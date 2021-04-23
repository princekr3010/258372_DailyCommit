# Write a python program to find the repeated items in a tuple.

def repeat(tuple_a):
    for i in range(0, len(tuple_a)):
        for j in range(i + 1, len(tuple_a)):
            if tuple_a[i] == tuple_a[j]:
                print(tuple_a[i], end="")
                print(" ", end="")


tuple_a = (1, 2, 3, 4, 1, 3, 5, 6, 7)
print("Repeated items are: ", end="")
repeat(tuple_a)


# Write a python program to list of tuples into a dictionary.



def Convert(tup, di):
    di = dict(tup)
    return di


tups = [("Atul", 17), ("gautam", 42), ("anand", 64),
        ("suraj", 90), ("Prakash", 26), ("Prince", 39)]
dictionary = {}
print (Convert(tups, dictionary))
