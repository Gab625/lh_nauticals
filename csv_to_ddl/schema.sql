DROP TABLE IF EXISTS brands;
CREATE TABLE brands (
    brand_id INTEGER,
    brand_name TEXT,
    brand_country TEXT,
    brand_is_active BOOL,
    brand_created_at TIMESTAMP,
    brand_update_at TIMESTAMP
);

DROP TABLE IF EXISTS categories;
CREATE TABLE categories (
    category_id INTEGER,
    category_name TEXT,
    slug TEXT,
    parent_category_id NUMERIC,
    category_is_active BOOL,
    category_created_at TIMESTAMP,
    category_updated_at TIMESTAMP
);

DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
    customer_id INTEGER,
    person_type TEXT,
    legal_name TEXT,
    trade_name TEXT,
    tax_id NUMERIC,
    state_registration TEXT,
    email TEXT,
    phone TEXT,
    customer_is_active BOOL,
    customer_created_at TIMESTAMP,
    customer_updated_at TIMESTAMP
);

DROP TABLE IF EXISTS locations;
CREATE TABLE locations (
    location_id INTEGER,
    location_name TEXT,
    location_type TEXT,
    postal_code TEXT,
    street TEXT,
    number INTEGER,
    complement TEXT,
    district TEXT,
    city TEXT,
    state TEXT,
    location_country TEXT,
    location_is_active BOOL,
    location_created_at TIMESTAMP,
    location_updated_at TIMESTAMP
);

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    order_id INTEGER,
    order_number TEXT,
    channel TEXT,
    customer_id INTEGER,
    salesperson_id NUMERIC,
    location_id INTEGER,
    status BOOL,
    subtotal NUMERIC,
    discount_amount NUMERIC,
    total NUMERIC,
    placed_at TEXT,
    order_created_at TIMESTAMP,
    order_updated_at TIMESTAMP
);

DROP TABLE IF EXISTS order_items;
CREATE TABLE order_items (
    order_item_id INTEGER,
    order_id INTEGER,
    product_variant_id INTEGER,
    quantity INTEGER,
    unit_price NUMERIC,
    items_icms_rate NUMERIC,
    items_ipi_rate NUMERIC,
    line_total NUMERIC
);

DROP TABLE IF EXISTS products;
CREATE TABLE products (
    product_id INTEGER,
    product_name TEXT,
    description TEXT,
    brand_id INTEGER,
    category_id INTEGER,
    ncm_code INTEGER,
    unit_of_measure TEXT,
    product_is_active BOOL,
    product_created_at TIMESTAMP,
    product_updated_at TIMESTAMP
);

DROP TABLE IF EXISTS product_variants;
CREATE TABLE product_variants (
    product_variant_id INTEGER,
    product_id INTEGER,
    sku TEXT,
    barcode_ean NUMERIC,
    sale_price NUMERIC,
    cost_price NUMERIC,
    weight_kg NUMERIC,
    variant_icms_rate NUMERIC,
    variant_ipi_rate NUMERIC,
    variant_is_active BOOL,
    variant_created_at TIMESTAMP,
    variant_updated_at TIMESTAMP
);

