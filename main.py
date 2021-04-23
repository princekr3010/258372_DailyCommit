def fun():
    list = [1, 2, 3, 4, 5]
    print(list[:-1])
    print(list[2:5])
    print(list[3:-1])
    l = list[1:3]
    l.append(8)
    l.insert(1, 9)
    l.remove(2)
    l.reverse()
    print(l)

    list_2d = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]
    print(list_2d)
    print(list_2d[1][3])
    list_2d.extend([[2, 3, 4, 5]])
    print(list_2d)
    print(list.index(3))
    list_2d.sort()
    print(list_2d)

    list3 = l[:-1].copy()
    print(list3)


fun()

