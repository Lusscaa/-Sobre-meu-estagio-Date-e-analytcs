arquivo_texto = '''Este conteúdo está em
um
arquivo
de texto.
'''

with open('arquivo_texto.txt', 'r') as f:
    conteudo = f.read()
    print(conteudo, end="")

