import pandas as pd
from pymongo import MongoClient
from config_log import obtener_logger

logger = obtener_logger("Extraccion")

class Extraccion:
    def __init__(self, uri, database_name):
        self.client = MongoClient(uri)
        self.db = self.client[database_name]
        logger.info(f"Conectado a MongoDB: {database_name}")

    def consultar_coleccion(self, nombre):
        try:
            df = pd.DataFrame(list(self.db[nombre].find()))
            logger.info(f"Extraccion OK: {nombre} ({len(df)} registros)")
            return df
        except Exception as e:
            logger.error(f"Error extrayendo {nombre}: {e}")
            return pd.DataFrame()

    def ejecutar_extraccion_completa(self):
        return {col: self.consultar_coleccion(col) for col in ['calendar', 'listings', 'reviews']}