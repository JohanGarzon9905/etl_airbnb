import pandas as pd
from config_log import obtener_logger
import re

logger = obtener_logger("Transformacion")

class Transformacion:
    def __init__(self, dataframes_dict):
        self.dfs = dataframes_dict
        logger.info("Fase de Transformacion iniciada.")

    def ejecutar_transformacion_completa(self):
        for nombre, df in self.dfs.items():
            for col in df.select_dtypes(include=['object']).columns:
                df[col] = df[col].apply(lambda x: re.sub(r'[^\x09\x0A\x0D\x20-\x7E\xA0-\xFF]', '', str(x)) if x else x)

            if 'date' in df.columns:
                df['date'] = pd.to_datetime(df['date'])
                logger.info(f"Fechas normalizadas en {nombre}")
            
            if nombre in ['listings', 'calendar'] and 'price' not in df.columns:
                logger.warning(f"ADVERTENCIA: 'price' no existe en {nombre}")
        
        return self.dfs