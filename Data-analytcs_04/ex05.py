from csv import reader

with open('estudantes.csv', encoding='utf-8') as listinha:
    ler = reader(listinha)
    for x in sorted(ler):
        aluno = x[0]
        notas = x[1:]
        notasint = list(map(int, notas))
        top3 = sorted(notasint, reverse=True)[:3]
        media = round(sum(top3) / 3, 2)

        print("Nome: {} Notas: {} Média: {}".format(aluno, top3, media))
