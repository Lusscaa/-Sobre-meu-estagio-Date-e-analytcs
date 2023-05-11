SELECT autor.codautor, autor.nome, COUNT(*) AS quantidade_publicacoes
FROM autor
JOIN livro 
	ON autor.codautor = livro.autor
GROUP BY autor.codautor
ORDER BY quantidade_publicacoes DESC
LIMIT 1