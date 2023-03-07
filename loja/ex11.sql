SELECT 
  tbvendas.cdcli, 
  tbvendas.nmcli, 
  SUM(tbvendas.vrunt * tbvendas.qtd) AS gasto
FROM 
  tbvendas
  INNER JOIN tbvendedor ON tbvendedor.cdvdd = tbvendas.cdvdd 
WHERE 
  tbvendas.status = 'Concluído'
GROUP BY 
  tbvendas.cdcli, tbvendas.nmcli
ORDER BY 
  gasto DESC
 LIMIT 1;