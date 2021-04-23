# write a program to get next day of a given date using if-elif-else.
import string

year = int(input("Input a year: "))

# checking for leap year
if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30


day = int(input("Input a day [1-31]: "))

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))


# Write a program to check the user input abbrevation.

statement = input("Enter your input: ")
if statement == "lol":
    print("laughing out loud")
elif statement == "rofl":
    print("rolling on the floor laughing")
elif statement == "lmk":
    print("let me know")
elif statement == "smh":
    print("shaking my head")
else:
    print("Enter correct input")


# Write a python code that asks a user how many pizza slices they want. The Pizzeria charges Rs123.00 for slice. If user order even number of slices, price per slice is Rs, 120.00. Print the toral price depending on how many slice user orders.


number_of_slice = int(input("Enter the number of slice you want:"))
price = 123
if number_of_slice%2==0:
    price = 120

print("Your Total Bill is: ", end="")
print(number_of_slice*price)

# Write a python program to check if the input number is
# -real number
# -float number
# -string
# -complex number
# -Zero (0)

value = eval(input("Enter the value"))

if isinstance(value, int):
    print("real number")
elif isinstance(value, float):
    print("float number")
elif isinstance(value, string):
    print("String")
elif isinstance(value, complex):
    print("complex number")
elif value==0:
    print("Zero (0)")
else:
    print("enter correct value")