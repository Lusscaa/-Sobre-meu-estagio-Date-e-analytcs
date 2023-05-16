faturamentos = {}
i = 0

with open("actors.csv", "r+", encoding="utf-8") as arquivo:
    for linha in arquivo:
        if '"Robert Downey, Jr."' in linha:
            linha = linha.replace('"Robert Downey, Jr."','"Robert Downey Jr."')
        if i == 0:
            i += 1
            continue
        l = linha.split(",")
        ator = l[0]
        faturamento_bruto = float(l[3])
        if ator in faturamentos:
            faturamentos[ator].append(faturamento_bruto)
        else:
            faturamentos[ator] = [faturamento_bruto]

for ator, faturamentos_brutos in faturamentos.items():
    media_faturamento = sum(faturamentos_brutos) / len(faturamentos_brutos)
    print('A media de faturamento bruto para {} é: {}'.format(ator, media_faturamento))

    with open('etapa-2.txt', 'a', encoding="utf-8") as arquivo2:
        arquivo2.write('A media de faturamento bruto para {} é: {}\n'.format(ator, media_faturamento))
