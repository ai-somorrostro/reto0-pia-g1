FROM nodered/node-red:3.1

USER node-red

RUN npm install node-red-contrib-influxdb

COPY /nodered/flows.json /data/flows.json

USER root