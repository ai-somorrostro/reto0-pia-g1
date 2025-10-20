# Documentacion Big Data Aplicado

## Jupyter Notebook 
Hemos creado un notebook el cual baja de la API los datos de criptomonedas y los sube a un bucket de influxdb para poder mostrar los datos usando python3 más pandas.

## Node Red
Hemos creado flujos de node red que obtendran datos de la API y los tratara para poder enviarlos a influxdb donde se guardan en un bucket para poder mostrarlos.

## Influxdb
Hemos creado un par de buckets que obtienen los datos de nuestro notebook y de node red y de esos buckets escogeremos los datos que queramos y creando un notebook y convirtiendolo en flujo lo enviaremos a grafana.

## Grafana
Hemos creado algunos paneles de control para la correcta visualizacion de los datos enviados desde influx en diferentes graficas y otra visualizacion con datos que hemos encontrado de buena relevancia a su vez tambien hemos creado alertas las cuales nos avisaran cuando algunos datos entren en un intervalo especificado y por ultimo tambien hemos creado unos cuantos grupos y usuarios que tienen diferentes permisos sobre los paneles de control ya sea de lectura y escritura o algun panel de control restringido.