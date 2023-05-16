SELECT cddep, nmdep, dtnasc, SUM(tbvendas.vrunt * tbvendas.qtd) AS valor_total_vendas
FROM tbdependente
LEFT JOIN tbvendas ON tbvendas.cdvdd  = tbdependente.cdvdd
WHERE tbvendas.status = 'Concluído'
GROUP BY tbvendas.cdvdd
ORDER BY valor_total_vendas
LIMIT 1