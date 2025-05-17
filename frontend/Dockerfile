# بناء الواجهة الأمامية
FROM node:20 AS builder

WORKDIR /app
COPY . .
RUN npm install && npm run build

# تقديم الواجهة باستخدام nginx
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html

