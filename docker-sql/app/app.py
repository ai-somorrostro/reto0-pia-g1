import os
import pyodbc
import urllib.request
import json
from datetime import datetime
import time
import socket

# -----------------------------
# Funciones auxiliares
# -----------------------------

def obtener_criptos():
    url = "https://api.coinlore.net/api/tickers/"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
        return data.get("data", [])

def esperar_sqlserver(host, port, timeout=60):
    start = time.time()
    while True:
        try:
            with socket.create_connection((host, port), timeout=2):
                return
        except OSError:
            if time.time() - start > timeout:
                raise TimeoutError("SQL Server no respondió a tiempo")
            print("⏳ SQL Server no listo, reintentando en 2s...")
            time.sleep(2)

# -----------------------------
# Conexión y creación DB
# -----------------------------

def conectar_db():
    server = os.getenv("DB_SERVER", "sqlserver")
    database = os.getenv("DB_NAME", "criptosdb")
    username = os.getenv("DB_USER", "sa")
    password = os.getenv("DB_PASSWORD", "TuPasswordSegura123")
    driver = "{ODBC Driver 18 for SQL Server}"

    # Conectarse a master con autocommit
    conn_master = None
    while True:
        try:
            conn_master = pyodbc.connect(
                f"DRIVER={driver};SERVER={server};DATABASE=master;UID={username};PWD={password};TrustServerCertificate=yes;",
                autocommit=True  # <- esto evita el error de CREATE DATABASE
            )
            break
        except pyodbc.Error:
            print("⏳ Esperando a que SQL Server acepte conexiones...")
            time.sleep(2)

    cursor = conn_master.cursor()
    cursor.execute(f"IF DB_ID('{database}') IS NULL CREATE DATABASE {database};")
    cursor.close()
    conn_master.close()

    # Conectarse a la base creada
    conn = pyodbc.connect(
        f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes;"
    )
    return conn

    server = os.getenv("DB_SERVER", "sqlserver")
    database = os.getenv("DB_NAME", "criptosdb")
    username = os.getenv("DB_USER", "sa")
    password = os.getenv("DB_PASSWORD", "TuPasswordSegura123")
    driver = "{ODBC Driver 18 for SQL Server}"

    # Conectarse primero a master para crear la base si no existe
    conn_master = None
    while True:
        try:
            conn_master = pyodbc.connect(
                f"DRIVER={driver};SERVER={server};DATABASE=master;UID={username};PWD={password};TrustServerCertificate=yes;"
            )
            break
        except pyodbc.Error:
            print("⏳ Esperando a que SQL Server acepte conexiones...")
            time.sleep(2)

    cursor = conn_master.cursor()
    cursor.execute(f"IF DB_ID('{database}') IS NULL CREATE DATABASE {database};")
    cursor.commit()
    cursor.close()
    conn_master.close()

    # Conectarse a la base creada
    conn = pyodbc.connect(
        f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes;"
    )
    return conn

# -----------------------------
# Crear tabla si no existe
# -----------------------------

def crear_tabla(conn):
    cursor = conn.cursor()
    cursor.execute("""
        IF OBJECT_ID('dbo.precios', 'U') IS NULL
        CREATE TABLE precios (
            id INT IDENTITY(1,1) PRIMARY KEY,
            crypto_id NVARCHAR(50),
            rank INT,
            price_usd FLOAT,
            percent_change_24h FLOAT,
            percent_change_7d FLOAT,
            price_btc FLOAT,
            fecha DATETIME
        )
    """)
    cursor.commit()
    cursor.close()

# -----------------------------
# Guardar datos
# -----------------------------

def guardar_datos(conn, monedas):
    cursor = conn.cursor()
    timestamp = datetime.now()
    for moneda in monedas:
        cursor.execute("""
            INSERT INTO precios (crypto_id, rank, price_usd, percent_change_24h, percent_change_7d, price_btc, fecha)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            moneda.get("id"),
            moneda.get("rank"),
            moneda.get("price_usd"),
            moneda.get("percent_change_24h"),
            moneda.get("percent_change_7d"),
            moneda.get("price_btc"),
            timestamp
        ))
    conn.commit()
    cursor.close()
    print(f"[{timestamp}] {len(monedas)} filas insertadas correctamente.")

# -----------------------------
# Programa principal
# -----------------------------

if __name__ == "__main__":
    print("⏳ Esperando que SQL Server esté listo...")
    esperar_sqlserver(os.getenv("DB_SERVER", "sqlserver"), 1433)

    conn = conectar_db()
    crear_tabla(conn)

    while True:
        monedas = obtener_criptos()
        if monedas:
            guardar_datos(conn, monedas)
        time.sleep(100)
