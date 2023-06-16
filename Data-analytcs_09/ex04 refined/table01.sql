CREATE TABLE filmes AS
SELECT  json.adult AS Adult,
        json.original_language AS Idioma,
        json.runtime AS Minutosdofilme,
        csv._c0 AS id,
        csv._c1 AS Titulo,
        csv._c2 AS Titulo_original,
        csv._c3 AS ano_lancamento,
        csv._c4 AS Tempo_Minuto,
        csv._c5 AS Genero,
        csv._c6 AS NotaMedia,
        csv._c7 AS Votos
FROM jsonneosoro AS json
JOIN csvneosorocopy as csv
ON json.imdb_id = csv._c0
WHERE _c5 LIKE '%Action%' OR _c5 LIKE '%Adventure%'