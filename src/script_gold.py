import pandas as pd
from pathlib import Path
from src.config import SILVER_DIR, GOLD_DIR, COLUNAS_GOLD

def carregar_dados_silver(diretorio_silver = SILVER_DIR, colunas_desejadas = COLUNAS_GOLD):
    caminho_pasta = Path(diretorio_silver)
    dados_silver = {}

    for tabela, colunas in colunas_desejadas.items():
        arquivo_csv = caminho_pasta / f"{tabela}.csv"

        if  not arquivo_csv.exists():
            dados_silver[tabela] = pd.read_csv(arquivo_csv, usecols=colunas)
            print("Aviso: {tabela}.csv nao encontrado na Silver. Pulando...")
            continue

        dados_silver[tabela] = pd.read_csv(arquivo_csv, usecols=colunas)

    return dados_silver

def run_gold():
    GOLD_DIR.mkdir(parents=True, exist_ok=True)

    tabelas = carregar_dados_silver()

    orders = tabelas.get("orders")
    locations = tabelas.get("locations")
    customers = tabelas.get("customers")
    order_items = tabelas.get("order_items")
    product_variants = tabelas.get("product_variants")
    products = tabelas.get("products")
    brands = tabelas.get("brands")
    categories = tabelas.get("categories")

    dias = {
        'Monday': 'Segunda-Feira',     # ou 'Segunda-feira' se preferir traduzir
        'Tuesday': 'Terça-Feira',
        'Wednesday': 'Quarta-Feira',
        'Thursday': 'Quinta-Feira',
        'Friday': 'Sexta-Feira',
        'Saturday': 'Sábado',
        'Sunday': 'Domingo'
    }

    df_join = (
        orders
        .merge(locations, on='location_id', how='inner')
        .merge(customers, on='customer_id', how='inner')
        .merge(order_items, on='order_id', how='inner')
        .merge(product_variants, on='product_variant_id', how='inner')
        .merge(products, on='product_id', how='inner')
        .merge(brands, on='brand_id', how='inner')
        .merge(categories, on='category_id', how='inner')
    )

    df_join = df_join[df_join['status'] == True].copy()
    df_join['data'] = pd.to_datetime(df_join['placed_at']).dt.date
    df_join['ano'] = pd.to_datetime(df_join['placed_at']).dt.year.astype(str)
    df_join['ano_mes'] = pd.to_datetime(df_join['placed_at']).dt.to_period('M').astype(str)
    df_join['dia_semana'] = pd.to_datetime(df_join['placed_at']).dt.day_name().map(dias)

    data_inicio = pd.to_datetime(df_join['placed_at']).min()
    data_fim = pd.to_datetime(df_join['placed_at']).max()

    calendario = pd.DataFrame({
        'data': pd.date_range(start=data_inicio, end=data_fim, freq='D').date
    })
    calendario['dia_semana'] = pd.to_datetime(calendario['data']).dt.day_name().map(dias)

    caminho_calendario = GOLD_DIR / "dim_calendar.csv"
    calendario.to_csv(caminho_calendario, index=False, encoding='utf-8-sig')

    caminho_fato = GOLD_DIR / "fato_consolidado.csv"
    df_join.to_csv(caminho_fato, index=False, encoding='utf-8-sig')

    print("Camada Gold processada com sucesso! Fato e Calendário salvos na pasta Gold.")

if __name__ == "__main__":
    run_gold()