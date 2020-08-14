FROM node:12.10.0

WORKDIR /usr/app

COPY package*.json ./

RUN npm i 

COPY . .

EXPOSE 3000

CMD ["npm", "run", "start:dev"]