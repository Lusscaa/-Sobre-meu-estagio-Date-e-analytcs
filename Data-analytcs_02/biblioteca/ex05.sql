SELECT DISTINCT autor.nome
FROM autor
LEFT JOIN livro 
ON autor.codautor = livro.autor
WHERE livro.editora != '13'
ORDER BY autor.nome ASC;