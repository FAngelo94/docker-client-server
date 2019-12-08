FROM node:8.7.0-alpine

# Create app directory and use it as the working directory
RUN mkdir -p /srv/app/fr-shohin-admin-server
WORKDIR /svr/app/fr-shohin-admin-server

COPY package.json /srv/app/fr-shohin-admin-server
copy package-lock.json /srv/app/fr-shohin-admin-server

RUN npm install

copy . /srv/app/fr-shohin-admin-server

CMD ["npm", "run", "start"]