FROM node:lts-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

ARG API_URL
ENV VUE_APP_API_URL=$API_URL

RUN npm install @vue/cli -g
RUN npm install serve -g

COPY . /app
COPY package.json .
COPY package-lock.json .

RUN npm install
RUN npm run build

CMD ["sh", "-c", "serve -s dist"]
