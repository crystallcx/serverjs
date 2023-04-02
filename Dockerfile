FROM node:alpine

WORKDIR /app

COPY app /app

CMD ["node","app.js"]