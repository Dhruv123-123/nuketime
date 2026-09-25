# One image with every toolchain the local judge needs: Node 22, Python 3, g++, JDK.
FROM node:22-bookworm

RUN apt-get update && apt-get install -y --no-install-recommends \
      python3 python3-pip g++ default-jdk-headless \
    && pip3 install --break-system-packages sortedcontainers requests \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY package.json package-lock.json* ./
COPY server/package.json server/
COPY web/package.json web/
RUN npm install

COPY . .
RUN npm run build

ENV PORT=3000
EXPOSE 3000
CMD ["npm", "start"]
