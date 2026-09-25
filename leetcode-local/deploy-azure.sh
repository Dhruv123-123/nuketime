#!/usr/bin/env bash
# Deploy to Azure Container Apps (you already have an Azure account for the AI model).
# Prereqs: `az login`, Docker not required (the image is built in the cloud by ACR).
# Usage: APP_PASSWORD=... AZURE_OPENAI_API_KEY=... ./deploy-azure.sh
set -euo pipefail

command -v az >/dev/null || { echo "Install the Azure CLI first: https://aka.ms/installazurecli"; exit 1; }
az account show >/dev/null 2>&1 || { echo "Run: az login"; exit 1; }

RG="${RG:-leetcode-local-rg}"
LOC="${LOC:-eastus}"
ACR="${ACR:-lclocal$RANDOM}"          # must be globally unique, lowercase
ENV_NAME="${ENV_NAME:-leetcode-local-env}"
APP="${APP:-leetcode-local}"
STORAGE="${STORAGE:-lcdata$RANDOM}"
: "${APP_PASSWORD:?set APP_PASSWORD}"
: "${AZURE_OPENAI_API_KEY:?set AZURE_OPENAI_API_KEY}"
AZURE_OPENAI_ENDPOINT="${AZURE_OPENAI_ENDPOINT:?set AZURE_OPENAI_ENDPOINT}"
AZURE_OPENAI_MODEL="${AZURE_OPENAI_MODEL:?set AZURE_OPENAI_MODEL}"

az extension add --name containerapp --upgrade -y >/dev/null 2>&1 || true

echo "Registering resource providers (a new subscription needs this once; takes a minute)..."
for ns in Microsoft.ContainerRegistry Microsoft.App Microsoft.OperationalInsights Microsoft.Storage; do
  az provider register --namespace "$ns" --wait >/dev/null
done
az group create -n "$RG" -l "$LOC" >/dev/null
az acr create -n "$ACR" -g "$RG" --sku Basic --admin-enabled true >/dev/null
echo "Building image in ACR..."
# APP_USER=root: Azure Files SMB mounts are root-owned, so the app must run as root to write /data.
az acr build -r "$ACR" -t leetcode-local:latest --build-arg APP_USER=root "$(dirname "$0")"

echo "Creating persistent storage for /data..."
az storage account create -n "$STORAGE" -g "$RG" -l "$LOC" --sku Standard_LRS >/dev/null
KEY=$(az storage account keys list -n "$STORAGE" -g "$RG" --query '[0].value' -o tsv)
az storage share-rm create --storage-account "$STORAGE" -n lcdata --quota 1 >/dev/null

az containerapp env create -n "$ENV_NAME" -g "$RG" -l "$LOC" >/dev/null
az containerapp env storage set -n "$ENV_NAME" -g "$RG" --storage-name lcdata \
  --azure-file-account-name "$STORAGE" --azure-file-account-key "$KEY" --azure-file-share-name lcdata --access-mode ReadWrite >/dev/null

ACR_PW=$(az acr credential show -n "$ACR" --query 'passwords[0].value' -o tsv)
az containerapp create -n "$APP" -g "$RG" --environment "$ENV_NAME" \
  --image "$ACR.azurecr.io/leetcode-local:latest" \
  --registry-server "$ACR.azurecr.io" --registry-username "$ACR" --registry-password "$ACR_PW" \
  --target-port 3000 --ingress external --cpu 1 --memory 2Gi --min-replicas 0 --max-replicas 1 \
  --secrets "app-password=$APP_PASSWORD" "ai-key=$AZURE_OPENAI_API_KEY" \
  --env-vars NODE_ENV=production LC_USER_DIR=/data APP_PASSWORD=secretref:app-password \
             AZURE_OPENAI_ENDPOINT="$AZURE_OPENAI_ENDPOINT" AZURE_OPENAI_API_KEY=secretref:ai-key \
             AZURE_OPENAI_MODEL="$AZURE_OPENAI_MODEL" AZURE_OPENAI_REASONING=low >/dev/null

# Mount the file share at /data (needs a YAML patch).
TMP=$(mktemp --suffix .json)
az containerapp show -n "$APP" -g "$RG" -o json > "$TMP"
python3 - "$TMP" <<'PY'
import sys, json
p = sys.argv[1]; d = json.load(open(p))
t = d['properties']['template']
t['volumes'] = [{'name': 'lcdata', 'storageType': 'AzureFile', 'storageName': 'lcdata'}]
t['containers'][0]['volumeMounts'] = [{'volumeName': 'lcdata', 'mountPath': '/data'}]
json.dump(d, open(p, 'w'))
PY
az containerapp update -n "$APP" -g "$RG" --yaml "$TMP" >/dev/null
echo
echo "Deployed. Open: https://$(az containerapp show -n "$APP" -g "$RG" --query properties.configuration.ingress.fqdn -o tsv)"
