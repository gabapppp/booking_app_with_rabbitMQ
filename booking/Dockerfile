FROM node:20-alpine3.19 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM node:20-alpine3.19 AS server
WORKDIR /app
COPY package* ./
RUN npm install --production
COPY --from=builder ./app/dist ./dist
EXPOSE 3366
CMD ["node", "dist/booking/src/app.js",]