idade = 0
linha_selecionada = []
i = 0
with open("actors.csv", "r+", encoding="utf-8") as arquivo:
    for linha in arquivo:
        if '"Robert Downey, Jr."' in linha:
            linha = linha.replace('"Robert Downey, Jr."','"Robert Downey Jr."')
        if i == 0:
            i += 1
            continue
        l = linha.split(",")
        if int(l[2]) > idade:
            idade = int(l[2])
            linha_selecionada = l

    x = linha_selecionada[0]
    y = linha_selecionada[2]

    
    print('O ator é {} com o maior numero, com um total de {} filmes.'.format(x, y))

    with open('etapa-1.txt', 'w', encoding="utf-8") as arquivo2:
        arquivo2.write('O ator é {} com o maior numero, com um total de {} filmes.'.format(x, y))

