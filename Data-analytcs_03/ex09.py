def remove_duplicados(lista):
    lista_sem_duplicados = list(set(lista))
    return lista_sem_duplicados

l1 = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
l2 = remove_duplicados(l1)
print(l2)
