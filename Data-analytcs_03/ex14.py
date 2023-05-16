def print_params(*args, **top2):
    for arg in args:
        print(arg)
    for value in top2.values():
        print(value)


print_params(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
