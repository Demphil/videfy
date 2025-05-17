FROM node:20-alpine
WORKDIR /frontend
COPY package.json vite.config.js tailwind.config.js postcss.config.js ./
COPY public ./public
COPY src ./src
RUN npm install
EXPOSE 3000
CMD ["npm", "run", "dev"]
