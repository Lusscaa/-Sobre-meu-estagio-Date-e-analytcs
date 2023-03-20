import random 

random_list = random.sample(range(500), 50)

valor_minimo = min(random_list)

valor_maximo = max(random_list)

media = sum(random_list) / len(random_list)

sorted_list = sorted(random_list)
tamanho = len(sorted_list)
if tamanho % 2 == 0:
    mediana = (sorted_list[int(tamanho/2)-1] + sorted_list[int(tamanho/2)]) / 2
else:
    mediana = sorted_list[int(tamanho/2)]



print(f"Media: {valor_minimo}, Mediana: {valor_maximo}, Mínimo: {media}, Máximo: {mediana}")