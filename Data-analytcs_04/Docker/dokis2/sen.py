import hashlib
while True:
    nome = (input(" Digite seu nome")).encode()
    x = hashlib.sha1(nome)
    print(x.hexdigest())