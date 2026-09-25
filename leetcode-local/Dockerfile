# One image with every toolchain the local judge needs: Node 22, Python 3, g++, JDK.
# Works locally (docker compose up) and on any container host (Render, Fly.io,
# Railway, Azure Container Apps, Cloud Run...).
FROM node:22-bookworm

RUN apt-get update && apt-get install -y --no-install-recommends \
      python3 python3-pip g++ default-jdk-headless curl \
    && pip3 install --break-system-packages sortedcontainers requests \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY package.json package-lock.json* ./
COPY server/package.json server/
COPY web/package.json web/
RUN npm install

COPY . .
RUN npm run build

# Optionally mirror statement images into the image (FETCH_IMAGES=1 adds ~80 MB).
ARG FETCH_IMAGES=0
RUN if [ "$FETCH_IMAGES" = "1" ]; then python3 scraper/fetch_images.py; fi

# Run as an unprivileged user; user data lives on a volume mounted at /data.
RUN useradd -m app && mkdir -p /data && chown -R app:app /app /data
USER app

ENV NODE_ENV=production \
    PORT=3000 \
    LC_USER_DIR=/data
EXPOSE 3000
HEALTHCHECK --interval=30s --timeout=5s --start-period=20s CMD curl -fsS http://localhost:3000/api/health || exit 1
CMD ["node", "server/src/index.js"]
