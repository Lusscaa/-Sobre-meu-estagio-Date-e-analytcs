for i in range(1, 4):
    num = int(input("Digite o número {}: ".format(i)))
    if num % 2 == 0:
        print("Par:", num)
    else:
        print("Ímpar:", num)