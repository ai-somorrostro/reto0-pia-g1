#!/bin/bash
echo "Iniciando SQL Server"
sudo chown -R 10001:0 sql_data/
sudo chmod -R 770 sql_data/
docker compose up -d
echo ""
echo "Servicios iniciados"
echo ""