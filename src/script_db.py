from pathlib import Path
import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from src.config import SILVER_DIR, SCHEMA_SCRIPT

load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

caminho_schema = SCHEMA_SCRIPT
caminho_csv = SILVER_DIR

DB_URI = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(DB_URI)

def run_exportation():
    try:
        with engine.begin() as conn:
            with open(caminho_schema, "r", encoding="utf-8") as f:
                sql_script = f.read()
            conn.execute(text(sql_script))
        print("Schema executado com sucesso!\n")
    except Exception as e:
        print(f"Erro ao executar o schema.sql: {e}")
        exit()

    for arquivo in caminho_csv.iterdir():
        if arquivo.suffix == ".csv":
            nome_tabela = arquivo.stem

            df = pd.read_csv(arquivo, encoding="utf-8")

            df.to_sql(
            name=nome_tabela,
            con=engine,
            if_exists="append",
            index=False,
            chunksize=1000,
        )

        print(f"Tabela '{nome_tabela}' importada com sucesso para o banco de dados.")

if __name__ == "__main__":
    run_exportation()