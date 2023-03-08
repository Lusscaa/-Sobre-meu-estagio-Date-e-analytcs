SELECT tbvendas.cdven
FROM tbvendas
LEFT JOIN tbvendedor ON tbvendas.cdven = tbvendedor.cdvdd
WHERE tbvendas.deletado <> 0