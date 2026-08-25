WITH periodo AS (
    SELECT
        MIN(placed_at::date) AS data_inicial,
        MAX(placed_at::date) AS data_final
    FROM orders
    WHERE channel = 'pos'
),

-- Cria o calendário com todos os dias do período
calendario AS (
    SELECT
        generate_series(
            data_inicial,
            data_final,
            INTERVAL '1 day'
        )::date AS data_calendario
    FROM periodo
),

-- Soma as vendas por dia
vendas_diarias AS (
    SELECT
        placed_at::date AS data_venda,
        SUM(total) AS valor_venda
    FROM orders
    WHERE channel = 'pos'
    GROUP BY placed_at::date
),

-- Cruza todos os dias do calendário com as vendas
vendas_calendario AS (
    SELECT
        c.data_calendario,
        COALESCE(v.valor_venda, 0) AS vendas
    FROM calendario c

    LEFT JOIN vendas_diarias v
        ON c.data_calendario = v.data_venda
)


SELECT
    EXTRACT(DOW FROM data_calendario) AS numero_dia_semana,

    CASE EXTRACT(DOW FROM data_calendario)
        WHEN 1 THEN 'Segunda-feira'
        WHEN 2 THEN 'Terça-feira'
        WHEN 3 THEN 'Quarta-feira'
        WHEN 4 THEN 'Quinta-feira'
        WHEN 5 THEN 'Sexta-feira'
        WHEN 6 THEN 'Sábado'
        WHEN 0 THEN 'Domingo'
    END AS dia_semana,

    AVG(vendas) AS media_vendas

FROM vendas_calendario

GROUP BY
    EXTRACT(DOW FROM data_calendario)

ORDER BY
    media_vendas desc;