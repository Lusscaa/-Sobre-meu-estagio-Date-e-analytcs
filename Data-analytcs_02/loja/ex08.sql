SELECT tbvendedor.cdvdd, tbvendedor.nmvdd
FROM tbvendedor
INNER JOIN tbvendas ON tbvendas.cdvdd = tbvendedor.cdvdd 
WHERE tbvendas.status = 'Concluído'
GROUP BY tbvendedor.cdvdd, tbvendedor.nmvdd
ORDER BY COUNT(*) DESC
LIMIT 1;