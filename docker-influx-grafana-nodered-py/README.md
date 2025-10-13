# USO DEL DOCKER PARA LEVANTAR LOS SERVICIOS DE INFLUX, NODERED, PYTHON CON PANDAS Y GRAFANA

## 1.- Clonar el repositorio

```
git clone git@github.com:ai-somorrostro/reto0-pia-g1.git
```

## 2.- Entrar en la carpeta del repo y en la carpete de docker-influx-grafana-nodered-py

```
cd reto0-pia-g1/docker-influx-grafana-nodered-py
```

## 3.- Ejecutar el siguiente comando para que levante los servicios

```
docker compose up -d
```

## 4.- Finalmente en el navegador acceder a las siguientes direcciones para cada servicio

**NodeRed**: http://localhost:1880
**InfluxDB**: http://localhost:8086  
**Grafana**: http://localhost:3000  