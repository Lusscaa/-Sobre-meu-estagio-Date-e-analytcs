SELECT cdpro, nmpro
FROM tbvendas
WHERE tbvendas.dtven BETWEEN '2014-02-03' AND '2018-02-02' AND status = 'Concluído'
LIMIT 1