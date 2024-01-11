FROM node:current-slim

RUN mkdir -p /app

WORKDIR /pp

COPY . .

RUN npm install


ENV NUXT_HOST=0.0.0.0

ENV NUXT_PORT=3000

ENV SERVER_URL='http://127.0.0.1:8000/todo/' 
ENV LOGIN_TOKEN='YWRtaW46YWRtaW4='

RUN npm run build

CMD [ "node", "./.output/server/index.mjs"]

EXPOSE 3000