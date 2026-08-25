DROP TABLE IF EXISTS addresses;
CREATE TABLE addresses (
    id INTEGER,
    customer_id INTEGER,
    address_type TEXT,
    postal_code TEXT,
    street TEXT,
    number INTEGER,
    complement TEXT,
    district TEXT,
    city TEXT,
    state TEXT,
    country TEXT,
    is_primary BOOL
);

DROP TABLE IF EXISTS attributes;
CREATE TABLE attributes (
    id INTEGER,
    name TEXT,
    data_type TEXT
);

DROP TABLE IF EXISTS brands;
CREATE TABLE brands (
    id INTEGER,
    name TEXT,
    country TEXT,
    is_active BOOL,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

DROP TABLE IF EXISTS categories;
CREATE TABLE categories (
    id INTEGER,
    name TEXT,
    slug TEXT,
    parent_category_id INTEGER,
    is_active BOOL,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
    id INTEGER,
    person_type TEXT,
    legal_name TEXT,
    trade_name TEXT,
    tax_id NUMERIC,
    state_registration TEXT,
    email TEXT,
    phone TEXT,
    is_active BOOL,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
    id INTEGER,
    full_name TEXT,
    cpf NUMERIC,
    email TEXT,
    role TEXT,
    primary_location_id INTEGER,
    hire_date TEXT,
    termination_date TEXT,
    is_active BOOL,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

DROP TABLE IF EXISTS fiscal_invoices;
CREATE TABLE fiscal_invoices (
    id INTEGER,
    order_id INTEGER,
    nfe_number TEXT,
    nfe_access_key NUMERIC,
    series INTEGER,
    issued_at TIMESTAMP,
    status TEXT,
    total_amount NUMERIC,
    xml_storage_uri TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

DROP TABLE IF EXISTS goods_receipts;
CREATE TABLE goods_receipts (
    id INTEGER,
    purchase_order_id INTEGER,
    received_by_employee_id INTEGER,
    received_at TIMESTAMP,
    notes TEXT,
    created_at TIMESTAMP
);

DROP TABLE IF EXISTS goods_receipt_items;
CREATE TABLE goods_receipt_items (
    id INTEGER,
    goods_receipt_id INTEGER,
    purchase_order_item_id INTEGER,
    quantity_received NUMERIC
);

DROP TABLE IF EXISTS locations;
CREATE TABLE locations (
    id INTEGER,
    name TEXT,
    location_type TEXT,
    postal_code TEXT,
    street TEXT,
    number INTEGER,
    complement TEXT,
    district TEXT,
    city TEXT,
    state TEXT,
    country TEXT,
    is_active BOOL,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    id INTEGER,
    order_number TEXT,
    channel TEXT,
    customer_id INTEGER,
    salesperson_id INTEGER,
    location_id INTEGER,
    status TEXT,
    subtotal NUMERIC,
    discount_amount NUMERIC,
    total NUMERIC,
    placed_at TIMESTAMP,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

DROP TABLE IF EXISTS order_items;
CREATE TABLE order_items (
    id INTEGER,
    order_id INTEGER,
    product_variant_id INTEGER,
    quantity INTEGER,
    unit_price NUMERIC,
    icms_rate NUMERIC,
    ipi_rate NUMERIC,
    line_total NUMERIC
);

DROP TABLE IF EXISTS payments;
CREATE TABLE payments (
    id INTEGER,
    order_id INTEGER,
    method TEXT,
    installments INTEGER,
    amount NUMERIC,
    status TEXT,
    paid_at TIMESTAMP,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

DROP TABLE IF EXISTS products;
CREATE TABLE products (
    id INTEGER,
    name TEXT,
    description TEXT,
    brand_id INTEGER,
    category_id INTEGER,
    ncm_code INTEGER,
    unit_of_measure TEXT,
    is_active BOOL,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

DROP TABLE IF EXISTS product_suppliers;
CREATE TABLE product_suppliers (
    product_variant_id INTEGER,
    supplier_id INTEGER,
    supplier_sku TEXT,
    last_quoted_cost NUMERIC,
    lead_time_days INTEGER,
    is_preferred BOOL,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

DROP TABLE IF EXISTS product_variants;
CREATE TABLE product_variants (
    id INTEGER,
    product_id INTEGER,
    sku TEXT,
    barcode_ean NUMERIC,
    sale_price NUMERIC,
    cost_price NUMERIC,
    weight_kg NUMERIC,
    icms_rate NUMERIC,
    ipi_rate NUMERIC,
    is_active BOOL,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

DROP TABLE IF EXISTS purchase_orders;
CREATE TABLE purchase_orders (
    id INTEGER,
    po_number TEXT,
    supplier_id INTEGER,
    buyer_id INTEGER,
    destination_location_id INTEGER,
    status TEXT,
    currency TEXT,
    subtotal NUMERIC,
    total NUMERIC,
    placed_at TIMESTAMP,
    expected_delivery_at TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

DROP TABLE IF EXISTS purchase_order_items;
CREATE TABLE purchase_order_items (
    id INTEGER,
    purchase_order_id INTEGER,
    product_variant_id INTEGER,
    quantity_ordered INTEGER,
    unit_cost NUMERIC,
    line_total NUMERIC
);

DROP TABLE IF EXISTS returns;
CREATE TABLE returns (
    id INTEGER,
    return_number TEXT,
    order_id INTEGER,
    customer_id INTEGER,
    received_at_location_id INTEGER,
    status TEXT,
    reason TEXT,
    total_refund_amount NUMERIC,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

DROP TABLE IF EXISTS return_items;
CREATE TABLE return_items (
    id INTEGER,
    return_id INTEGER,
    order_item_id INTEGER,
    quantity NUMERIC,
    action TEXT,
    exchange_variant_id INTEGER,
    unit_refund_amount NUMERIC
);

DROP TABLE IF EXISTS stock_levels;
CREATE TABLE stock_levels (
    product_variant_id INTEGER,
    location_id INTEGER,
    quantity_on_hand NUMERIC,
    reorder_point TEXT,
    updated_at TIMESTAMP
);

DROP TABLE IF EXISTS stock_movements;
CREATE TABLE stock_movements (
    id INTEGER,
    product_variant_id INTEGER,
    location_id INTEGER,
    movement_type TEXT,
    quantity NUMERIC,
    reference_table TEXT,
    reference_id INTEGER,
    employee_id INTEGER,
    notes TEXT,
    occurred_at TIMESTAMP,
    created_at TIMESTAMP
);

DROP TABLE IF EXISTS suppliers;
CREATE TABLE suppliers (
    id INTEGER,
    legal_name TEXT,
    trade_name TEXT,
    country TEXT,
    tax_id TEXT,
    tax_id_type TEXT,
    email TEXT,
    phone NUMERIC,
    contact_name TEXT,
    is_active BOOL,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

DROP TABLE IF EXISTS variant_attribute_values;
CREATE TABLE variant_attribute_values (
    product_variant_id INTEGER,
    attribute_id INTEGER,
    value TEXT
);

