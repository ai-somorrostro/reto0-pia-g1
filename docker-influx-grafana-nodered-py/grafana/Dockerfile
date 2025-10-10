FROM grafana/grafana:10.3.0

# Copiar el dashboard
COPY grafana/dashboards/ /etc/grafana/provisioning/dashboards/

# Copiar el archivo de provisioning
COPY grafana/provisioning/dashboards/dashboards.yml /etc/grafana/provisioning/dashboards/

# Copiar el archivo de datasource
COPY grafana/provisioning/datasources/influxdb.yml /etc/grafana/provisioning/datasources/
