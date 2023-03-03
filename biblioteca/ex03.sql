SELECT
    count(*) as quantidade,
    ed.nome,
    en.estado,
    en.cidade
FROM Livro as li
INNER JOIN editora as ed
    ON li.editora =  ed.codeditora
INNER JOIN endereco as en
    ON ed.endereco = en.codendereco
GROUP BY  ed.nome
ORDER BY quantidade desc
LIMIT 5