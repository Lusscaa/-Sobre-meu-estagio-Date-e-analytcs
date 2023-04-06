with open('number.txt', "r") as arquivo:
    dados = arquivo.readlines()

    num = list(map(int,dados))

par = filter(lambda x:x%2==0,num)

ordem = sorted(par, reverse=True)

cinco = ordem[:5]

print(cinco)
print(sum(cinco))