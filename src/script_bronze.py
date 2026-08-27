import pandas as pd
from src.config import RAW_DIR, BRONZE_DIR, TABELAS_SELECIONADAS

def load_bronze():
    BRONZE_DIR.mkdir(parents=True, exist_ok=True)

    for tabela in TABELAS_SELECIONADAS:
        arquivo_raw = RAW_DIR / f"{tabela}.csv"

        if arquivo_raw.exists():
            df = pd.read_csv(arquivo_raw)

            caminho_destino = BRONZE_DIR / f"{tabela}.csv"
            df.to_csv(caminho_destino, index=False)
            print(f"[BRONZE] Tabela '{tabela}' processada com sucesso")
        else:
            print(f"[BRONZE] Erro '{tabela}.csv' não encontrada")

if __name__ == "__main__":
    load_bronze()