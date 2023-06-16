CREATE TABLE atores AS
SELECT  _c8 AS generoArtista,
        _c9 AS personagem,
        _c10 AS nomeArtista,
        _c11 AS anoNascimento,
        _c12 AS anoFalecimento,
        _c13 AS profissao,
        _c14 AS titulosMaisConhecidos,
        _c0 AS idfilme
FROM csvneosorocopy
WHERE _c5 LIKE '%Action%' OR _c5 LIKE '%Adventure%'