#!/usr/bin/env bash
# Deploy to Azure Container Apps (you already have an Azure account for the AI model).
# Prereqs: `az login`, Docker not required (the image is built in the cloud by ACR).
# Usage: APP_PASSWORD=... AZURE_OPENAI_API_KEY=... ./deploy-azure.sh
set -euo pipefail

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

az extension add --name containerapp --upgrade -y >/dev/null
az group create -n "$RG" -l "$LOC" >/dev/null
az acr create -n "$ACR" -g "$RG" --sku Basic --admin-enabled true >/dev/null
echo "Building image in ACR..."
az acr build -r "$ACR" -t leetcode-local:latest "$(dirname "$0")"

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
  --secrets "appPassword=$APP_PASSWORD" "aiKey=$AZURE_OPENAI_API_KEY" \
  --env-vars NODE_ENV=production LC_USER_DIR=/data APP_PASSWORD=secretref:appPassword \
             AZURE_OPENAI_ENDPOINT="$AZURE_OPENAI_ENDPOINT" AZURE_OPENAI_API_KEY=secretref:aiKey \
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
echo "Deployed: https://$(az containerapp show -n "$APP" -g "$RG" --query properties.configuration.ingress.fqdn -o tsv)"
