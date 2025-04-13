import os
from dotenv import load_dotenv
from google import genai
# Carrega variáveis do arquivo .env
load_dotenv()

class Config:
    # Correção: Adicione o nome da variável de ambiente entre aspas
    client = genai.Client(api_key='AIzaSyBDn0K7nqSJh_bcgM8JJU3vCCVmnTLX-Zo')
    TEMPLATES_AUTO_RELOAD = True
    