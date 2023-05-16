class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada
    
    def ordenacaoCrescente(self):
        return sorted(self.listaBaguncada)
    
    def ordenacaoDecrescente(self):
        return sorted(self.listaBaguncada, reverse=True)


lista_crescente = [3, 4, 2, 1, 5]
lista_decrescente = [9, 7, 6, 8]

crescente = Ordenadora(lista_crescente)
decrescente = Ordenadora(lista_decrescente)
crescente_ordenado = crescente.ordenacaoCrescente()
decrescente_ordenado = decrescente.ordenacaoDecrescente()

print(crescente_ordenado)
print(decrescente_ordenado)
