SELECT 
	tbvendas.cdpro, 
	tbvendas.nmcanalvendas, 
	tbvendas.nmpro, 
	SUM(qtd) AS quantidade_vendas
FROM tbvendas
WHERE tbvendas.status = 'Concluído'
GROUP BY 
	tbvendas.nmcanalvendas, 
	tbvendas.nmpro
ORDER BY quantidade_vendas
LIMIT 10