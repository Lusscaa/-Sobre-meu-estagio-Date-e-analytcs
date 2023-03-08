SELECT 
	TBVENDAS.estado, 
	ROUND(AVG(vrunt * qtd), 2) AS gastomedio
FROM tbvendas
WHERE tbvendas.status = 'Concluído'
GROUP BY estado
ORDER BY gastomedio desc