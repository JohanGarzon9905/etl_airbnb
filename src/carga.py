import sqlite3
import pandas as pd
import os
import re
from config_log import obtener_logger

logger = obtener_logger("Carga")

class Carga:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.db_path = os.path.join(self.base_dir, "airbnb_analitico.db")
        self.report_dir = os.path.join(self.base_dir, "reportes")

    def insertar_sqlite(self, data_dict):
        try:
            conn = sqlite3.connect(self.db_path)
            for tabla, df in data_dict.items():
                df_sql = df.copy()
                for col in df_sql.columns:
                    if df_sql[col].apply(lambda x: isinstance(x, (list, dict))).any():
                        df_sql[col] = df_sql[col].astype(str)
                df_sql.to_sql(tabla, conn, if_exists='replace', index=False)
                logger.info(f"Carga SQL OK: {tabla}")
            conn.close()
        except Exception as e:
            logger.error(f"FALLO SQLITE: {e}")

    def exportar_excel(self, data_dict):
        if not os.path.exists(self.report_dir):
            os.makedirs(self.report_dir)
            
        for nombre, df in data_dict.items():
            ruta_excel = os.path.join(self.report_dir, f"{nombre}.xlsx")
            
            df_excel = df.copy()
            for col in df_excel.select_dtypes(include=['object']).columns:
                df_excel[col] = df_excel[col].apply(
                    lambda x: re.sub(r'[^\x09\x0A\x0D\x20-\x7E\xA0-\xFF]', '', str(x)) if x else x
                )

            if len(df_excel) > 1000000:
                logger.warning(f"TABLA GRANDE: {nombre} excedio limite Excel. Usando muestra.")
                df_excel.head(500000).to_excel(ruta_excel, index=False)
            else:
                df_excel.to_excel(ruta_excel, index=False)
            logger.info(f"Excel guardado: {nombre}")

    def verificar_carga(self, data_dict):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        for tabla, df in data_dict.items():
            try:
                cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
                count = cursor.fetchone()[0]
                if count == len(df):
                    logger.info(f"VERIFICACION OK: {tabla} ({count} registros)")
                else:
                    logger.error(f"DISCREPANCIA: {tabla} - SQL: {count} vs DF: {len(df)}")
            except Exception as e:
                logger.error(f"No se pudo verificar la tabla {tabla}: {e}")
        conn.close()