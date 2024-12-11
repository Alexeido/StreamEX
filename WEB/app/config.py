import os
from dotenv import load_dotenv

# Cargar el contenido del .env en las variables de entorno del sistema
load_dotenv()

class Config:
    DEBUG = True
    STATIC_FOLDER = 'static'
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY') 
    API_BASE_URL = 'http://127.0.0.1:8000'