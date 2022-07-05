num1 = 42
# variable declaration, initialize integer
num2 = 2.3
# variable declaration, initialize float
boolean = True
# variable declaration, initialize boolean
string = 'Hello World'
# variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# variable declaration, list type, initialize string
person = {'name': 'John', 'location': 'Salt Lake',
          'age': 37, 'is_balding': False}
# variable declaration, dictionary type, initialize string, boolean, number
fruit = ('blueberry', 'strawberry', 'banana')
# variable declaration, tuples type, initialize string


print(type(fruit))
# class tuple
print(pizza_toppings[1])
# Sausage
pizza_toppings.append('Mushrooms')
# add value at list, Mushrooms will ble pizza_toppings[5]
print(person['name'])
# John
person['name'] = 'George'
# chage vale at dictionary
person['eye_color'] = 'blue'
# add value at dictionary
print(fruit[2])
# banana

if num1 > 45:
    print("It's greater")
# conditional - if
else:
    print("It's lower")
# conditional - else, num1 = 42 thus "Its'lower"


if len(string) < 5:
    print("It's a short word!")
# conditional - if
elif len(string) > 15:
    print("It's a long word!")
# conditional - else if
else:
    print("Just right!")
# conditional - else, string is 11 thus "Just Right"

for x in range(5):
    print(x)
# for loop, start at 0, stop at 4, increment 1
for x in range(2, 5):
    print(x)
# for loop, start at 2, stop at 4, increment 1

for x in range(2, 10, 3):
    print(x)
x = 0
# # for loop, start at 2, stop at 9, increment 3

while(x < 5):
    print(x)
    x += 1
# while loop, start at 0, stop at 4, increment 1

pizza_toppings.pop()
# list type, delete value ('olives')
pizza_toppings.pop(1)
# list type, delete value ('sausage')

print(person)
person.pop('eye_color')
print(person)
# - KeyError: 'eye_color'

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
# for loop, start at pepperoni, break at Olives


def print_hello_ten_times():
    for num in range(10):
        print('Hello')


print_hello_ten_times()
# for loop, 10 times Hello print


def print_hello_x_times(x):
    for num in range(x):
        print('Hello')


print_hello_x_times(4)
# for loop, 4 times Hello print


def print_hello_x_or_ten_times(x=10):
    for num in range(x):
        print('Hello')


print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)
# for loop, 14 times Hello print

"""
Bonus section
"""

# print(num3)
# NameError: name 'num3' is not defined.
num3 = 72
# - variable declaration, , initialize integer
fruit[0] = 'cranberry'
# TypeError: 'tuple' object does not support item assignment
print(person['favorite_team'])
# KeyError: 'favorite_team'
print(pizza_toppings[7])
# IndexError: list index out of range
print(boolean)
# boolean type
fruit.append('raspberry')
# AttributeError: 'tuple' object has no attribute 'append'
fruit.pop(1)
# AttributeError: 'tuple' object has no attribute 'pop'
