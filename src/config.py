from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DADOS_DIR = BASE_DIR / "dados"

RAW_DIR = DADOS_DIR / "raw"
BRONZE_DIR = DADOS_DIR / "bronze"
SILVER_DIR = DADOS_DIR / "silver"
GOLD_DIR = DADOS_DIR / "gold"

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

COLUNAS_GOLD = {
    "brands" : ["brand_id", "brand_name"],
    "categories" : ["category_id", "category_name"],
    "customers" : ["customer_id", "person_type", "legal_name"],
    "locations" : ["location_id", "location_name", "state"],
    "order_items" : ["order_item_id", "order_id", "product_variant_id", "quantity", "unit_price", "line_total"],
    "orders" : ["order_id", "channel", "total", "placed_at", "location_id", "customer_id", "status"],
    "product_variants" : ["product_variant_id", "cost_price", "product_id"],
    "products" : ["product_id", "product_name", "brand_id", "category_id"],  
}