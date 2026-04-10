# Pipeline ETL - Airbnb Buenos Aires 2026

## 1. Descripcion del proyecto y objetivo
Este proyecto implementa un proceso ETL (Extraccion, Transformacion y Carga) sobre datos de Airbnb para Buenos Aires.

Objetivo principal:
- Extraer datos desde MongoDB.
- Limpiar y estandarizar los datos para analitica.
- Cargar los resultados en SQLite y generar reportes en Excel.
- Mantener trazabilidad del proceso mediante logs en la carpeta logs.

## 2. Instrucciones de instalacion

### 2.1 Creacion del entorno virtual
En la raiz del proyecto:

```bash
python -m venv venv
```

Activacion del entorno:

Windows (PowerShell):

```bash
.\venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source venv/bin/activate
```

### 2.2 Instalacion de dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 2.3 Ejecucion del proyecto
La ejecucion del flujo completo se realiza desde el notebook:

```bash
jupyter notebook notebooks/ETL.ipynb
```

Luego ejecutar todas las celdas (Run All).

Resultado esperado:
- Carga de tablas en airbnb_analitico.db
- Generacion de reportes Excel en la carpeta reportes
- Registro del proceso en archivos de la carpeta logs

## 3. Integrantes del grupo y responsabilidades

| Integrante | Responsabilidades |
|---|---|
| Johan Sneider Garzón Salazar | Extraccion desde MongoDB, configuracion del entorno, carga en SQLite, exportacion a Excel y monitoreo de logs del proceso |
| Juan Esteban Daza Buitrago | Transformacion y limpieza de datos, validacion de calidad e integridad, analisis exploratorio en notebooks y documentacion del proyecto |

## 4. Ejemplo de ejecucion del proceso ETL
Ejemplo de secuencia al correr el notebook ETL:

```text
21:45:41 - [Extraccion] - INFO - Conectado a MongoDB: AirbnbBuenosAires
21:45:41 - [Extraccion] - INFO - Extraccion OK: calendar (... registros)
21:45:42 - [Transformacion] - INFO - Fase de Transformacion iniciada.
21:45:45 - [Carga] - INFO - Carga SQL OK: listings
21:45:46 - [Carga] - INFO - Excel guardado: listings
21:45:47 - [Carga] - INFO - VERIFICACION OK: listings (... registros)

Proceso finalizado exitosamente.
```

## 5. Estructura del proyecto

```text
etl_airbnb-main/
|-- src/
|   |-- extraccion.py
|   |-- transformacion.py
|   |-- carga.py
|   |-- config_log.py
|-- notebooks/
|   |-- ETL.ipynb
|   |-- exploracion_airbnb.ipynb
|-- logs/
|-- requirements.txt
|-- README.md
```