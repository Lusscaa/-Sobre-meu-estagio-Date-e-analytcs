def list_full(list):
    xlist1 = int((len(list) / 3))
    xlist2 = xlist1 * 2
    ylist1 = list[:xlist1]
    ylist2 = list[xlist1:xlist2]
    ylist3 = list[xlist2:]
    print(ylist1,ylist2, ylist3)


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
list_full(list)
