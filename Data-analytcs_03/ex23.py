class Calculo:
    def soma(self, x, y):
        return x + y
    
    def subtracao(self, x, y):
        return x - y


x = 4
y = 5

calc = Calculo()

soma = calc.soma(x, y)
subtracao = calc.subtracao(x, y)

print(f"Somando: {x}+{y} = {soma}")
print(f"Subtraindo: {x}-{y} = {subtracao}")
