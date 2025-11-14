# Стадия зависимостей
FROM node:16-alpine as deps
WORKDIR /app
# package-lock.json will appear after npm install
COPY package*.json .
RUN npm ci

# Стадия тестирования
FROM deps as test
COPY . .
CMD npm run lint && npm run test

# Стадия production
FROM node:16-alpine
RUN adduser --disabled-password nodeuser
WORKDIR /app
COPY package*.json server.js .
COPY --from=deps /app/node_modules ./node_modules
RUN npm prune --production
USER nodeuser
EXPOSE 3000
CMD npm start

# docker build --target test -t multinode:test .
# docker build -t multinode:prod .
# docker run -p 3000:3000 --name multinode multinode:prod
