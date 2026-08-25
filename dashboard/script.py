import pandas as pd

df_products = pd.read_csv("../dados/1-lh_nautical_csv/products.csv")
df_product_variants = pd.read_csv("../dados/1-lh_nautical_csv/product_variants.csv")
df_order_items = pd.read_csv("../dados/1-lh_nautical_csv/order_items.csv")
df_orders = pd.read_csv("../dados/1-lh_nautical_csv/orders.csv")
df_locations = pd.read_csv("../dados/1-lh_nautical_csv/locations.csv")
df_categories = pd.read_csv("../dados/1-lh_nautical_csv/categories.csv")
df_brands = pd.read_csv("../dados/1-lh_nautical_csv/brands.csv")
df_customers = pd.read_csv("../dados/1-lh_nautical_csv/customers.csv")


orders = df_orders.rename(columns={
    'id': 'order_id', 
    'is_active': 'order_is_active',
    'created_at': 'order_created_at',
    'updated_at': 'order_updated_at'
})

customers = df_customers.rename(columns={
    'id':'customer_id',
    'is_active':'customer_is_active',
    'created_at':'customer_created_at',
    'updated_at':'customer_updated_at'
})

locations = df_locations.rename(columns={
    'id':'location_id',
    'name':'location_name',
    'country':'location_country',
    'is_active':'location_is_active',
    'created_at':'location_created_at',
    'updated_at':'location_updated_at'
})

order_items = df_order_items.rename(columns={
    'id': 'order_item_id',
    'icms_rate': 'items_icms_rate',
    'ipi_rate': 'items_ipi_rate'
})

variants = df_product_variants.rename(columns={
    'id': 'product_variant_id', 
    'is_active': 'variant_is_active',
    'created_at': 'variant_created_at',
    'updated_at': 'variant_updated_at',
    'icms_rate': 'variant_icms_rate',
    'ipi_rate': 'variant_ipi_rate'
})

products = df_products.rename(columns={
    'id': 'product_id',
    'name':'product_name',
    'is_active': 'product_is_active', 
    'created_at': 'product_created_at',
    'updated_at': 'product_updated_at'
})

brands = df_brands.rename(columns={
    'id':'brand_id',
    'is_active':'brand_is_active',
    'created_at':'brand_created_at',
    'updated_at':'brand_update_at',
    'name':'brand_name',
    'country':'brand_country'
})

categories = df_categories.rename(columns={
    'id': 'category_id',
    'name':'category_name',
    'is_active':'category_is_active',
    'created_at':'category_created_at',
    'updated_at':'category_updated_at'
})

dias = {
    'Monday': 'Segunda',
    'Tuesday': 'Terça',
    'Wednesday': 'Quarta',
    'Thursday': 'Quinta',
    'Friday': 'Sexta',
    'Saturday': 'Sábado',
    'Sunday': 'Domingo'
}

df_join = (
    orders
    .merge(locations, on='location_id', how='inner')
    .merge(customers, on='customer_id', how='inner')
    .merge(order_items, on='order_id', how='inner')
    .merge(variants, on='product_variant_id', how='inner')
    .merge(products, on='product_id', how='inner')
    .merge(brands, on='brand_id', how='inner')
    .merge(categories, on='category_id', how='inner')
)

df_join = df_join[df_join['status'] == 'paid'].copy()
df_join['data'] = pd.to_datetime(df_join['placed_at']).dt.date
df_join['ano'] = pd.to_datetime(df_join['placed_at']).dt.year.astype(str)
df_join['ano_mes'] = pd.to_datetime(df_join['placed_at']).dt.to_period('M').astype(str)
df_join['dia_semana'] = pd.to_datetime(df_join['placed_at']).dt.day_name().map(dias)
df_join = df_join.rename(columns={
    'line_total':'faturamento'
})

df_join['dia_semana'] = df_join['dia_semana']

df_join['custo_total'] = (
    df_join['quantity'] * df_join['cost_price']
)

df_join['lucro'] = (
    df_join['faturamento'] - df_join['custo_total']
)

colunas_selecionadas = [    
    'product_id',
    'product_name',
    'category_id',
    'category_name',
    'brand_id',
    'brand_name',
    'quantity',
    'unit_price',
    'faturamento',
    'custo_total',
    'lucro',
    'order_id',
    'customer_id',
    'channel',
    'location_id',
    'location_name',
    'location_country',
    'state',
    'status',
    'placed_at',
    'data',
    'ano',
    'ano_mes',
    'dia_semana',
    'legal_name'
]

df_final = df_join[
    
    colunas_selecionadas
].copy()

df_final.to_csv('fato_consolidado.csv', 
                index=False, sep=",", 
                encoding='utf-8-sig')
print("CSV gerado com sucesso!")

data_inicio = df_final['data'].min()
data_fim = df_final['data'].max()

calendario = pd.DataFrame({
    'data': pd.date_range(
        start=data_inicio,
        end=data_fim,
        freq='D'
    )
})

calendario.to_csv(
    'calendario.csv',
    index=False,
    encoding='utf-8-sig'
)

print("calendário gerado com sucesso!")