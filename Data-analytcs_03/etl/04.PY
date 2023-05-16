filmes_frequentes = {}
with open("actors.csv", "r+", encoding="utf-8") as arquivo:
    for linha in arquivo:
        if '"Robert Downey, Jr."' in linha:
            linha = linha.replace('"Robert Downey, Jr."','"Robert Downey Jr."')
        l = linha.split(",")
        nome_filme = l[4]
        if nome_filme not in filmes_frequentes:
            filmes_frequentes[nome_filme] = 1
        else:
            filmes_frequentes[nome_filme] += 1

# Encontrando o(s) filme(s) com a frequência mais alta
maior_frequencia = max(filmes_frequentes.values())
filmes_mais_frequentes = [filme for filme, frequencia in filmes_frequentes.items() if frequencia == maior_frequencia]

# Imprimindo o(s) filme(s) mais frequente(s) e sua respectiva frequência
print("O(s) filme(s) mais frequente(s) é(são):")
for filme in filmes_mais_frequentes:
    print("- {} ({} vezes)".format(filme, filmes_frequentes[filme]))

with open('etapa-4.txt', 'w', encoding="utf-8") as arquivo2:
    arquivo2.write("O(s) filme(s) mais frequente(s) é(são):\n")
    for filme in filmes_mais_frequentes:
        arquivo2.write("- {} ({} vezes)\n".format(filme, filmes_frequentes[filme]))
