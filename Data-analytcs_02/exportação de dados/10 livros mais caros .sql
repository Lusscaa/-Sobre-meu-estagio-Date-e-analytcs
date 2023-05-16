SELECT 
	livro.cod AS CodLivro, 
    livro.titulo AS Titulo, 
    autor.codautor AS CodAutor, 
    autor.nome AS NomeAutor, 
    livro.valor AS Valor, 
    editora.codeditora AS CodEditora, 
    editora.nome AS NomeEditora
FROM livro
LEFT JOIN editora ON livro.editora = editora.codeditora
LEFT JOIN autor ON editora.codeditora = autor.codautor
ORDER BY livro.valor DESC
LIMIT 10