compra_v = True
dados = 'Compra confirmada'

for enviar in range(3):
    if compra_v:
        print(dados)
        print("Datalhes enviado com sucesso")
        break # Parar quando o a compra for confirmada
    else:
        print("deu erroo")