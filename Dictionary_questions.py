# Write a python script to merge two python dictionaries.


def Merge(dict1, dict2):
    res = dict1 | dict2
    return res


dict1 = {'x': 15, 'y': 18, 'z': 21}
dict2 = {'a': 6, 'b': 4}
print("dictionary 1: ", end="")
print(dict1)
print("dictionary 2: ", end="")
print(dict2)
dict3 = Merge(dict1, dict2)
print("dictionary after merging:  ", end="")
print(dict3)


# write a program to convert a list into a nested dictionary of keys.

def fun():
    num_list = [1, 2, 3, 4, 5, 6, 7]
    new_dict = current_dict = {}
    for name in num_list:
        current_dict[name] = {}
        current_dict = current_dict[name]
    print(new_dict)


fun()
