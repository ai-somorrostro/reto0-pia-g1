# Uso del contenedor de docker para la creacion de base de datos y subsecuentes tablas de forma automatizada

## Clonar el repositorio
```
git clone git@github.com:ai-somorrostro/reto0-pia-g1.git
```

## Entrar en la carpeta del repo y en la carpeta de "docker-sql"
```
cd reto0-pia-g1/docker-sql
```

## Para iniciar los servicios hay que darle permiso al start.sh y ejecutarlo
```
chmod +x start.sh
```

```
./start.sh
```

## Para parar los servicios hay que darle permiso al stop.sh y ejecutarlo
```
chmod +x stop.sh
```

```
./stop.sh
```

## Entrar al servidor SQL
Introducir los datos de autenticacion de SQL Server para poder entrar y ver todos los datos siendo:   
**Nombre del servidor**:la ip de tu maquina virtual,1433 en mi caso fue "10.221.155.215,1433", el **usuario**:"sa" y la **password**:"TuPasswordSegura123"