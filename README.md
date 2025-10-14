# reto0-pia-g1

## Rama "docker-influx-grafana-nodered-py"
En esta rama estan todos los archivos necesarios para poder ejecutar el contenedor que inicializara influx, node red y grafana ademas del archivo python+pandas el cual junto a los flujos de node red se ejecutan cada 3 minutos.

## Rama "docker-csv"
En esta rama estan todos los archivos necesarios para poder ejecutar el contenedor que recogera datos de la api y cargar estos en un csv que ira agregando datos nuevos cada 3 minutos.

## Rama "docker-sql"
En esta rama estan todos los archivos necesarios para poder ejecutar el contenedor que recogera datos de la api y los cargara en una tabla de una base de datos en nuestro servidor de maquina virtual, si esta tabla o base de datos no estan creadas las creara para poder agregar los datos cada 3 minutos.

## Rama "docker-sql"
En esta rama estan todos los archivos necesarios para poder ejecutar el contenedor que inicializara el sqlserver

## Rama "githubpage" 
En esta rama estan todos los archivos necesarios para modificar y ejecutar nuestra Githubpage.

## Rama "gh-pages" 
Esta es una rama que se crea automaticamente al realizar el deploy de nuestra githubpage que incluye los htmls, css, fonts y demas que dan aspecto a nuestra pagina.

# Merges 
Hemos realizado una serie de merges entre las ramas "docker-influx-grafana-nodered-py", "githubpage", "docker-csv" y "docker-sql" contra master cada una de ellas por separado.
