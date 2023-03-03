SELECT
    count(*) as quantidade,
    A.nome,
    B.estado,
    B.cidade
FROM Livro as C
INNER JOIN editora as A 
    ON C.editora = B.codeditora
INNER JOIN endereco as B
    ON B.endereco = B.codendereco
GROUP BY A.nome
ORDER BY quantidade desc
LIMIT 5




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