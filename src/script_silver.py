import pandas as pd
from src.config import BRONZE_DIR, SILVER_DIR, TABELAS_SELECIONADAS

def padronizar_colunas(df, tabela):
    """Função renomeia colunas dos csvs"""
    mapeamento_colunas = {
        "orders" : {
            "id": "order_id", 
            "is_active": "order_is_active",
            "created_at": "order_created_at",
            "updated_at": "order_updated_at"
        },

        "customers" : {
            "id":"customer_id",
            "is_active":"customer_is_active",
            "created_at":"customer_created_at",
            "updated_at":"customer_updated_at"
        },

        "locations" : {
            "id":"location_id",
            "name":"location_name",
            "country":"location_country",
            "is_active":"location_is_active",
            "created_at":"location_created_at",
            "updated_at":"location_updated_at"
        },

        "order_items" : {
            "id": "order_item_id",
            "icms_rate": "items_icms_rate",
            "ipi_rate": "items_ipi_rate"
        },

        "product_variants" : {
            "id": "product_variant_id", 
            "is_active": "variant_is_active",
            "created_at": "variant_created_at",
            "updated_at": "variant_updated_at",
            "icms_rate": "variant_icms_rate",
            "ipi_rate": "variant_ipi_rate"
        },

        "products" : {
            "id": "product_id",
            "name":"product_name",
            "is_active": "product_is_active", 
            "created_at": "product_created_at",
            "updated_at": "product_updated_at"
        },

        "brands" : {
            "id":"brand_id",
            "is_active":"brand_is_active",
            "created_at":"brand_created_at",
            "updated_at":"brand_update_at",
            "name":"brand_name",
            "country":"brand_country"
        },

        "categories" : {
            "id": "category_id",
            "name":"category_name",
            "is_active":"category_is_active",
            "created_at":"category_created_at",
            "updated_at":"category_updated_at"
        }
    }

    if tabela in mapeamento_colunas:
        df = df.rename(columns=mapeamento_colunas[tabela])

    return df

def limpar_tabela_geral(df):
    """Aplica limpezas basicas comuns a todas as tabelas."""
    # 1. Remove linhas completamente duplicadas
    df = df.drop_duplicates()
    
    # 2. Remove espacos em branco nas pontas de colunas do tipo texto (string)
    colunas_texto = df.select_dtypes(include=["object"]).columns
    for col in colunas_texto:
        df[col] = df[col].astype(str).str.strip()
        
    return df

def drop_falses(df):
    colunas_bool = df.select_dtypes(include=["bool", "boolean"]).columns
    if not colunas_bool.empty:
        df = df[df[colunas_bool].all(axis=1)]

    return df

def aplicar_formatacao(df):
    colunas_format = {
        "brand_name",
        "category_name",
        "legal_name",
        "location_name",
        "product_name"
    }

    if "product_name" in df.columns:
        df["product_name"] = df["product_name"].replace(
                {"João da Silva": "Motor de Popa 000000"}
            )
    if "status" in df.columns:
        df["status"] = df["status"] == "paid"

    if "placed_at" in df.columns:
        df["placed_at"] = pd.to_datetime(df["placed_at"]).dt.normalize()
        
    for col in colunas_format:
        if col in df.columns:
            df[col] = df[col].astype(str).str.title()
    
    return df


def run_silver():
    SILVER_DIR.mkdir(parents=True, exist_ok=True)
    
    for tabela in TABELAS_SELECIONADAS:
        caminho_bronze = BRONZE_DIR / f"{tabela}.csv"
        
        if not caminho_bronze.exists():
            print(f"[SILVER] Aviso: {tabela}.csv nao encontrado na Bronze. Pulando...")
            continue
            
        # 1. Le da Bronze
        df = pd.read_csv(caminho_bronze)

        df = padronizar_colunas(df, tabela)
        df = aplicar_formatacao(df)
        df = drop_falses(df)
        # 2. Aplica limpezas gerais
        df = limpar_tabela_geral(df)
            
        # 4. Salva na Silver em CSV com UTF-8 para garantir acentuacao no Looker Studio
        caminho_silver = SILVER_DIR / f"{tabela}.csv"
        df.to_csv(caminho_silver, index=False, encoding="utf-8")
        
        print(f"[SILVER] Tabela '{tabela}' tratada e salva com sucesso.")

if __name__ == "__main__":
    run_silver()