import datetime

now = datetime.datetime.now()

nome = input("Digite seu nome: ")

cidade = input("Digite a cidade em que você nasceu: ")

anoDeNascimento = int(input("Digite o ano que você nasceu: "))

idade = now.year - anoDeNascimento

print("Sua idade é: " + str(idade))

print(nome + ", você terá " + str(idade + 10) + " anos daqui à 10 anos")