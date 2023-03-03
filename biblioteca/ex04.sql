SELECT
    au.nome,
    au.codautor,
    au.nascimento,
    COALESCE(COUNT(li.cod), 0) AS quantidade
FROM autor as au
LEFT JOIN livro as li ON li.autor = au.codautor
GROUP BY au.codautor, au.nome, au.nascimento
ORDER BY au.nome