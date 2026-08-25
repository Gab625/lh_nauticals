-- Quantidade total de linhas
-- Intervalo de datas analisado (data mínima e máxima)
-- Valor mínimo
-- Valor máximo
-- Valor médio
select 
	count(*) as contagem_total_registros,
	min(o.created_at::date) as data_inicial,
	max(o.created_at::date) as data_final,
	round(min(total),2) as menor_valor,
	round(max(total),2) as maior_valor,
	round(avg(total),2) as medias_valores
	
from orders o;  

-- Contagem de valores nulos em salesperson_id
SELECT COUNT(*) AS total_nulos
FROM orders o
WHERE salesperson_id IS null;

-- Cálculo de outliers
WITH calculo_quartis AS (
    SELECT 
        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY total) AS q1,
        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY total) AS q3
    FROM orders
),
limites AS (
    SELECT 
        q1,
        q3,
        (q3 - q1) AS iqr,
        q3 + 1.5 * (q3 - q1) AS limite_superior
    FROM calculo_quartis
)
SELECT COUNT(o.*) AS quantidade_outliers 
FROM orders o
CROSS JOIN limites l
WHERE o.total > l.limite_superior;

--output(452)

