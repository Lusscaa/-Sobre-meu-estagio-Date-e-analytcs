def my_map(lst, f):
    return [f(x) for x in lst]


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = lambda x: x ** 2
result = my_map(lst, f)
print(result)