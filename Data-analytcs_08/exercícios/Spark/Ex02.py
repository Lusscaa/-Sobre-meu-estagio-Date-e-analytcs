from pyspark.sql import SparkSession

# Inicializar SparkSession
spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

# Carregar arquivo nomes_aleatorios.txt em um dataframe
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True)

# Renomear a coluna para "Nomes"
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

# Mostrar o esquema do dataframe e as primeiras 10 linhas
df_nomes.printSchema()
df_nomes.show(10)

# Adicionar coluna "Escolaridade" com valores aleatórios
df_nomes = df_nomes.withColumn("Escolaridade", spark.when(spark.rand() < 1/3, "Fundamental")
                                             .when(spark.rand() < 2/3, "Medio")
                                             .otherwise("Superior"))

# Adicionar coluna "Pais" com nomes de países da América do Sul aleatórios
paises = ["Brasil", "Argentina", "Colômbia", "Venezuela", "Peru", "Chile", "Equador", "Bolívia", "Paraguai", "Uruguai", "Guiana", "Suriname", "Guiana Francesa"]
df_nomes = df_nomes.withColumn("Pais", spark.randomElement(paises))

# Adicionar coluna "AnoNascimento" com valores de ano aleatórios entre 1945 e 2010
df_nomes = df_nomes.withColumn("AnoNascimento", spark.expr("CAST(FLOOR(RAND() * (2010 - 1945 + 1) + 1945) AS INT)"))

# Selecionar pessoas que nasceram neste século
df_select = df_nomes.filter(df_nomes["AnoNascimento"] >= 2000)
df_select.show(10)

# Registrar dataframe como tabela temporária para uso com Spark SQL
df_nomes.createOrReplaceTempView("pessoas")

# Executar consulta Spark SQL para selecionar pessoas que nasceram neste século
spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2000").show(10)

# Contar o número de pessoas que são da geração Millennials usando o método select do dataframe
count_millennials = df_nomes.filter((df_nomes["AnoNascimento"] >= 1980) & (df_nomes["AnoNascimento"] <= 1994)).count()
print("Número de pessoas da geração Millennials (1980-1994):", count_millennials)

# Repetir a contagem usando Spark SQL
count_millennials_sql = spark.sql("SELECT COUNT(*) FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994").collect()[0][0]
print("Número de pessoas da geração Millennials (1980-1994) usando Spark SQL:", count_millennials_sql)

# Obter quantidade de pessoas de cada país para diferentes gerações usando Spark SQL
geracoes = {
    "Baby Boomers": (1944, 1964),
    "Geração X": (1965, 1979),
    "Millennials (Geração Y)": (1980, 1994),
    "Geração Z": (1995, 2015)
}

df_quantidade_por_pais = spark.sql("""
    SELECT Pais, COUNT(*) AS Quantidade
    FROM pessoas
    WHERE AnoNascimento BETWEEN {} AND {}
    GROUP BY Pais
    ORDER BY Pais, Quantidade
""".format(geracoes["Baby Boomers"][0], geracoes["Geração Z"][1]))

df_quantidade_por_pais.show()

