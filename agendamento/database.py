import os
import psycopg2
from dotenv import load_dotenv

load_dotenv(override=True)

def conectar():
    url = os.getenv("DATABASE_URL")

    if not url:
        raise ValueError("DATABASE_URL não foi configurada no .env")

    return psycopg2.connect(url)