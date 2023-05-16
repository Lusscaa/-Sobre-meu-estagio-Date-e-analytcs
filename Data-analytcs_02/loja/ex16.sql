SELECT 
	estado, 
	nmpro,
	ROUND(AVG(tbvendas.qtd), 4) AS quantidade_media
FROM tbvendas
WHERE status = 'Concluído'
GROUP BY estado, nmpro 