FROM nodered/node-red:3.1

USER node-red

RUN npm install node-red-contrib-influxdb

COPY /nodered/flows.json /data/flows.json
COPY /nodered/flows_cred.json /data/flows_cred.json
COPY /nodered/settings.js /data/settings.js

USER root