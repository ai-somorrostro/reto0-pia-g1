import urllib.request
import json
import csv
import os
import logging
from datetime import datetime
 
# Configuración de logging estructurado
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)
 
def obtener_criptos():
    url = "https://api.coinlore.net/api/tickers/"
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            return json.loads(data)
    except Exception as e:
        logger.error("Error al hacer la petición: %s", e)
        return None
 
 
if __name__ == "__main__":
    criptos = obtener_criptos()
    if criptos:
        monedas = criptos.get("data", [])
 
        # Columnas del CSV
        columnas_precio = ["rank", "price_usd", "percent_change_24h",
                           "percent_change_7d", "price_btc", "date", "id"]
 
        # Nombre fijo del archivo
        nombre_archivo = "/data/precio.csv"
 
        # Timestamp para la columna "date"
        timestamp_fila = datetime.now().isoformat()
 
        # Verificar si el archivo ya existe
        archivo_existe = os.path.exists(nombre_archivo)
 
        # Abrir en modo "append" para agregar al final sin borrar lo anterior
        with open(nombre_archivo, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=columnas_precio)
 
            # Si el archivo es nuevo, escribir encabezados
            if not archivo_existe:
                writer.writeheader()
 
            # Escribir las nuevas filas
            for moneda in monedas:
                row = {k: moneda.get(k) for k in columnas_precio if k != "date"}
                row["date"] = timestamp_fila
                writer.writerow(row)
 
        logger.info("Datos agregados correctamente a '%s'", nombre_archivo)
    else:
        logger.warning("No se pudieron obtener datos de criptomonedas")
