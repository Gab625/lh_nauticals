from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DADOS_DIR = BASE_DIR / "dados"

RAW_DIR = DADOS_DIR / "raw"
BRONZE_DIR = DADOS_DIR / "bronze"
SILVER_DIR = DADOS_DIR / "silver"

TABELAS_SELECIONADAS = [
    "brands",
    "categories",
    "customers",
    "locations",
    "order_items",
    "orders",
    "product_variants",
    "products"
]