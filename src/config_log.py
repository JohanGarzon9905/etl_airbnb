import logging
import sys
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, "logs")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

class ColoresSutilesFormatter(logging.Formatter):
    """Formateador para consola con colores sutiles (sin fondo)"""
    yellow = "\x1b[1;33m"
    red = "\x1b[1;31m"
    reset = "\x1b[0m"
    
    def format(self, record):
        fmt = f"%(asctime)s - [%(name)s] - %(levelname)s - %(message)s"
        if record.levelno == logging.ERROR:
            log_fmt = f"{self.red}{fmt}{self.reset}"
        elif record.levelno == logging.WARNING:
            log_fmt = f"{self.yellow}{fmt}{self.reset}"
        else:
            log_fmt = fmt
        return logging.Formatter(log_fmt, datefmt='%H:%M:%S').format(record)

def obtener_logger(nombre_proceso):
    logger = logging.getLogger(nombre_proceso)
    
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        logger.propagate = False

        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        log_filename = os.path.join(LOG_DIR, f"log_{nombre_proceso.lower()}_{timestamp}.txt")

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(ColoresSutilesFormatter())
        
        file_handler = logging.FileHandler(log_filename, encoding='utf-8')
        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
    
    return logger