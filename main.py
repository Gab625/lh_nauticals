from src.config import SCHEMA_SCRIPT, SILVER_DIR
from src.script_gold import run_gold
from src.script_bronze import run_bronze
from src.script_silver import run_silver
from src.script_db import run_exportation
from csv_to_ddl.ddl import csv_to_ddl

def main():
    print("Executando camada BRONZE")
    run_bronze()

    print("Executando camada SILVER")
    run_silver()

    print("Executando camada GOLD")
    run_gold()

    print("Executando script DDL")
    csv_to_ddl(caminho_csv=SILVER_DIR, arquivo_saida=SCHEMA_SCRIPT)

    print("Executando script de exportação para o banco de dados")
    run_exportation()

if __name__ == "__main__":
    main()