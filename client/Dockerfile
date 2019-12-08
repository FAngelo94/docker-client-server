FROM node:12.13

# Create app directory and use it as the working directory
RUN mkdir -p /srv/app/fr-shohin-admin-client

COPY . /srv/app/fr-shohin-admin-client

WORKDIR /srv/app/fr-shohin-admin-client

RUN npm install

CMD ["npm","start"]