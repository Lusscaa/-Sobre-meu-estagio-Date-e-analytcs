for num in range(2, 101):
    for div in range(2, num):
        if num % div == 0:
            break
    else:
        print(num)