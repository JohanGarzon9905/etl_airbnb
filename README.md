# Pipeline ETL - Airbnb Buenos Aires 2026

## 1. Descripción y Objetivo
Este proyecto implementa un proceso de **Extracción, Transformación y Carga (ETL)** para los datos de Airbnb en CABA. El objetivo es automatizar la migración de datos desde MongoDB hacia SQLite y reportes en Excel, asegurando la limpieza de caracteres especiales y la trazabilidad mediante logs profesionales.

## 2. Instrucciones de Instalación

### Creación del Entorno Virtual
```bash
python -m venv venv
# Activar en Windows: 
.\venv\Scripts\activate

# Activar en macOS/Linux: 
source venv/bin/activate