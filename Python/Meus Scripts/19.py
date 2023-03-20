v = int(input("digite o valor do seu produto: "))
while v >20:
    v = (v * 0.10) + v
    print(f"o valor final do seu produto sera: {v}")
    break