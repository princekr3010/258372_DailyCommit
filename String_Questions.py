# Write a python program to get a string from a given string share all occurances of its first char have been
# replaced to "$", except yhe first char itself.

str = input("Enter the string: ")
print(str[0], end="")
for i in range(1, len(str)):
    if str[0] == str[i]:
        print("$", end="")
    else:
        print(str[i], end="")

# Write a python program to find the first repeated character in a given string.

str = input("Enter the string: ")
flag = 0
for i in range(0, len(str)):
    for j in range(i + 1, len(str)):
        if str[i] == str[j]:
            print(str[j])
            flag = 1
            break
    if flag == 1:
        break


# Write a python program to remove nth element form a nonempty string.

def remove(string, n):
    first = string[:n]
    last = string[n + 1:]
    return first + last


print(remove("restart", 5))
