SELECT DISTINCT  autor.nome
FROM autor
LEFT JOIN livro 
	ON autor.codautor  = livro.autor
WHERE livro.autor IS NULL
ORDER BY nome
