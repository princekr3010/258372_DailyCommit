# Write a python program to find the second smallest number in a list.

def find_2nd_smallest(list_a):
    length = len(list_a)
    list_a.sort()
    print("Second Smallest element is:", list_a[1])


list_a=[23, 49, 2, 43, 35, 10, 89, 61, 47]
find_2nd_smallest(list_a)


# Write a python program to change the position of n-th value with the (n+1)th in a list.

def change_position(list_b, n):
    if len(list_b)>=n+2:
        list_b[n], list_b[n+1] = list_b[n+1], list_b[n]
        print(list_b)
    else:
        print("Incorrect position  ")


list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Before Changing Position: ", end="")
print(list_b)
print(len(list_b))
print("After Changing Position: ", end="")
change_position(list_b, 5)
