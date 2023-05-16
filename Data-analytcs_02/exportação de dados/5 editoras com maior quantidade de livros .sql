SELECT 
  editora.codeditora AS CodEditora,
  editora.nome AS NomeEditora,
  COUNT(*) AS QuantidadeLivros
FROM 
  livro
LEFT JOIN editora ON livro.editora = editora.codeditora
GROUP BY 
  CodEditora,
  NomeEditora
ORDER BY 
  QuantidadeLivros DESC
LIMIT 5;