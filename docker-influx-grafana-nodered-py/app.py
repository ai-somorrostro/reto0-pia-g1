import pandas as pd
import requests
import os
import logging
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WriteOptions, BucketsApi
from influxdb_client.client.exceptions import InfluxDBError
 
# Configuración de logging estructurado
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)
 
INFLUX_URL = os.environ.get("INFLUX_URL")
TOKEN = os.environ.get("INFLUX_TOKEN")
ORG = os.environ.get("INFLUX_ORG")
BUCKET = os.environ.get("INFLUX_BUCKET_PANDAS")
 
# Creamos el bucket de pandas en influx
with InfluxDBClient(url=INFLUX_URL, token=TOKEN, org=ORG) as client:
    # Creamos el bucket si no existe
    buckets_api = BucketsApi(client)
    try:
        bucket_list = buckets_api.find_buckets().buckets
        if not any(b.name == BUCKET for b in bucket_list):
            logger.info("Bucket '%s' no existe, creando...", BUCKET)
            buckets_api.create_bucket(bucket_name=BUCKET, org=ORG)
        else:
            logger.info("Bucket '%s' ya existe", BUCKET)
    except InfluxDBError as e:
        logger.error("Error al listar o crear bucket: %s", e)
        raise
 
# Cogemos los datos de la API y los pasamos a JSON
 
endpoint = "https://api.coinlore.net/api/tickers"
response = requests.get(endpoint)
 
if response.status_code == 200:
    data = response.json()
else:
    raise Exception(f"Error al obtener datos: {response.status_code}")
 
# Pasamos el JSON a DataFrame
 
coins = data['data']
df = pd.DataFrame(coins)
 
df_coins = df[['symbol','name','price_usd','rank','percent_change_24h','percent_change_7d','price_btc']].copy()
 
df_coins = df_coins[(df_coins['symbol'] == 'BTC') | (df_coins['symbol'] == 'ETH') | (df_coins['symbol'] == 'BNB') | (df_coins['symbol'] == 'XRP') | (df_coins['symbol'] == 'USDT') | (df_coins['symbol'] == 'SOL') | (df_coins['symbol'] == 'USDC') | (df_coins['symbol'] == 'SOON') | (df_coins['symbol'] == 'STETH')]
 
# Establecemos date y lo ponemos como indice
df_coins['date'] = pd.to_datetime(datetime.now())
 
df_coins = df_coins.set_index('date')
 
# Subimos los datos a Influx
try:
    with InfluxDBClient(url=INFLUX_URL, token=TOKEN, org=ORG) as client:
        write_api = client.write_api(write_options=WriteOptions(batch_size=1))
        try:
            for _, row in df_coins.iterrows():
               
                    p = (
                        Point("Criptomonedas")
                        .tag("symbol", row["symbol"])
                        .field("rank", int(row["rank"]))
                        .field("price_usd", float(row["price_usd"]))
                        .field("percent_change_24h", float(row["percent_change_24h"]))
                        .field("percent_change_7d", float(row["percent_change_7d"]))
                        .field("price_btc", float(row["price_btc"]))
                    )
                    write_api.write(bucket=BUCKET, org=ORG, record=p)
            logger.info("Registrados correctamente")
        except Exception as e:
            logger.error("Error registrando: %s", e)
        write_api.__del__()
       
except Exception as e:
    logger.error("Error de conexión con InfluxDB: %s", e)
