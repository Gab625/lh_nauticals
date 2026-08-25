	-- O Ticket Médio e a Diversidade de categorias por cliente.
-- A identificação e filtro dos 10 clientes "Fiéis" (maior Ticket Médio entre aqueles com diversidade >= 13 categorias).
with tb_diversidade_categoria as (
	select 
		t1.customer_id as cliente,
		count(distinct t5.id) as total_categorias_distintas
	from orders as t1
	left join order_items as t2
	on t1.id = t2.order_id
	left join product_variants as t3
	on t2.product_variant_id = t3.id
	left join products as t4
	on t3.product_id = t4.id
	left join categories as t5
	on t4.category_id = t5.id
	where t1.status = 'paid'
	group by t1.customer_id
	having count(distinct t5.id) >= 13
)
select
	   t3.legal_name as cliente,
	   SUM(t1.total) / COUNT(t1.id) as ticket_medio
from orders as t1
join tb_diversidade_categoria as t2
on t1.customer_id = t2.cliente
join customers as t3
on t1.customer_id = t3.id
where status = 'paid'
group by t1.customer_id, t3.legal_name
order by
	ticket_medio desc,
	t1.customer_id asc
limit 10;

--Calcule o Ticket Médio e a Diversidade de Categorias para cada customer_id.
--Filtre os 10 clientes com o maior Ticket Médio que atendam ao critério de diversidade (13 ou + categorias).
--Para este grupo específico de 10 clientes, 
--identifique qual categoria de produto concentra a maior quantidade total de itens comprados (sum(quantity)).

with tb_diversidade_categoria as (
	select 
		t1.customer_id as cliente,
		count(distinct t5.id) as total_categorias_distintas
	from orders as t1
	left join order_items as t2
	on t1.id = t2.order_id
	left join product_variants as t3
	on t2.product_variant_id = t3.id
	left join products as t4
	on t3.product_id = t4.id
	left join categories as t5
	on t4.category_id = t5.id
	where t1.status = 'paid'
	group by t1.customer_id
	having count(distinct t5.id) >= 13
),

tb_ticket_medio_10 as (
	select
	    t1.customer_id as cliente,
	    SUM(t1.total) / COUNT(t1.id) as ticket_medio
	from orders as t1
	join tb_diversidade_categoria as t2
	on t1.customer_id = t2.cliente
	where status = 'paid'
	group by t1.customer_id
	order by
		ticket_medio desc,
		t1.customer_id asc
	limit 10

)

select
	t6.name as categoria,
	sum(t3.quantity) as total_itens_comprados

from orders as t1

join tb_ticket_medio_10 as t2
on t1.customer_id = t2.cliente

join order_items as t3
on t1.id = t3.order_id

join product_variants as t4
on t3.product_variant_id = t4.id

join products as t5
on t4.product_id = t5.id

join categories as t6
on t5.category_id = t6.id

where t1.status = 'paid'

group by t6.name
	
order by total_itens_comprados desc

limit 1;

--output(Equipamentos)




