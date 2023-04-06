media = []
ator = []
c = 0
with open("actors.csv", "r+", encoding="utf-8") as arquivo:
    arquivo = arquivo.read().replace('"Robert Downey, Jr."','"Robert Downey Jr."').split('\n')

    
    for linha in arquivo[1:]:
        ator.append(linha.split(",")[0])
        media.append(float(linha.split(",")[3]))
    for m in media:
        if m == max(media):
          vv = (m)
          v = (ator[c])
        c += 1
with open("etapa-3.txt", "w", encoding="utf-8") as arquivo2:
    arquivo2.write("o {} tem o maior faturamento de {} por filme".format(v, vv))


            





'''print('O ator/atriz com a maior média de faturamento por filme é {} com uma média de faturamento de {} por filme.'.format(ator_maior_media, maior_media))

with open('etapa-3.txt', 'w', encoding="utf-8") as arquivo2:
    arquivo2.write('O ator/atriz com a maior média de faturamento por filme é {} com uma média de faturamento de {} por filme.'.format(ator_maior_media, maior_media))
'''
