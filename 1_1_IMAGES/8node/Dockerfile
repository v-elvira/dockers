FROM node:16
WORKDIR /app
COPY package*.json .
RUN npm install
COPY fetch.js .
ENV API_URL=https://jsonplaceholder.typicode.com/todos/1 FETCH_INTERVAL=5000
CMD ["node", "fetch.js"]
