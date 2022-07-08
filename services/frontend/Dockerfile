FROM node:lts-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH
ENV VUE_APP_API_URL=https://prueba-toteat-api.herokuapp.com/

RUN npm install @vue/cli@4.5.13 -g

RUN npm install -g serve

COPY . /app
COPY package.json .
COPY package-lock.json .

RUN npm install
RUN npm run build

CMD ["sh", "-c", "serve -s dist"]
