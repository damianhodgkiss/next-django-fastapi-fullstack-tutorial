FROM node:21-bookworm AS base
ARG DEBIAN_FRONTEND=noninteractive

ENV PORT 3000
ENV HOSTNAME "0.0.0.0"
# ENV NEXT_TELEMETRY_DISABLED 1

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
  libc6-dev \
  libvips-dev \
  build-essential \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN chown node:node /app


## Install dependencies based on the preferred package manager, and build the app
FROM base AS builder
USER root

# COPY package.json yarn.lock* package-lock.json* pnpm-lock.yaml* ./
COPY --chown=node:node . .
USER node
RUN \
  if [ -f yarn.lock ]; then yarn config set global-folder /app/.yarn && yarn --frozen-lockfile; \
  elif [ -f package-lock.json ]; then npm ci; \
  elif [ -f pnpm-lock.yaml ]; then yarn global add pnpm && pnpm i --frozen-lockfile; \
  else echo "Lockfile not found." && exit 1; \
  fi

RUN yarn build

## Copy the built app to a new image
FROM base AS runner
COPY --from=builder --chown=node:node /app/public ./public
COPY --from=builder --chown=node:node /app/.next/standalone ./
COPY --from=builder --chown=node:node /app/.next/static ./.next/static
COPY --from=builder --chown=node:node /app/node_modules/ ./node_modules/

USER node
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/app/node_modules/.bin
EXPOSE 3000
CMD ["node", "server.js"]