cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# and or
age1 = 20
age2 = 25
print(age1 >= 30 and age2 >= 22)
print(age1 >= 30 or age2 >= 22)

# in, not in
print('--in not in')
letters = ['a', 'b', 'c']
print('a' in letters)
print('y' in letters)
print('y' not in letters)

# test 5-1
print('\n# test 5-1')
cars = ['Daz', 'bmw', 'subaru', 'toyota', 'hava', 'qir', 'BYD', 'honda']
print(cars[0] == 'Daz')
print(cars[0] == 'Da')
print(cars[1] == 'Daz')
print(cars[1] == 'bmw')
print(cars[2] == 'subaru')
print(cars[2] == 'subaru ')
print(cars[3] == 'toyota')
print(cars[3] == ' toyota')

print('\n# test 5-2')
print(cars[-1] == 'honda')
print(cars[0] != 'Daz')
print(cars[-2].lower() == 'byd')

print('\n3 >= 3')
print(3 >= 3)

if 6 > 5:
    print('6>5')

print('\n# and or')
print(5 >= 0 and 1 > 5)
print(5 >= 0 or 1 > 5)

print('\n# in/ not in')
print('Daz' in cars)
print('Daz' not in cars)

# lession 5-3-1
print('\n# lession 5-3-1')
age = 16
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')
else:
    print('You are too young to vote.')

print('\n# elif')
ages = [4, 5, 16, 19]
for age in ages:
    if age <= 4:
        print(age)
        print('You are no more than 4 year old, free for you.')
    elif age < 18:
        print(age)
        print('You need to pay 5$.')
    else:
        print(age)
        print('You need to pay 10$.')

# test 5-3
print('\n# test 5-3')
alien_color = 'green2'
if alien_color == 'green':
    print('Player get 5 points!')
else:
    print('Target missed.')

# test 5-4
print('\n# test 5-4')
alien_color = 'green'
if alien_color == 'green':
    print('Player get 5 points!')
else:
    print('Player get 10 points!')

# test 5-5
print('\n# test 5-5')
alien_colors = ['green', 'red', 'yellow']
for color in alien_colors:
    if color == 'green':
        print('Player get 5 points!')
    elif color == 'yellow':
        print('Player get 10 points!')
    elif color == 'red':
        print('Player get 15 points!')

# lession 5.4.2
print('\n# lession 5.4.2')
list = []
if list:
    print('list not empty')
else:
    print('list is empty')

# lession 5.4.3
print('\n# lession 5.4.3 多个list')
available_toppings = ['盐', '味精', '辣椒', '糖']
request_toppings = ['味精', '蒜', '辣椒']

for requset in request_toppings:
    if requset in available_toppings:
        print('Adding ' + requset + '.')
    else:
        print('Sorry, we dont have ' + requset)

# test 5-11
print('\n#test 5-11')
for i in range(1, 10):
    if i == 1:
        print(str(i) + 'st')
    elif i == 2:
        print(str(i) + 'nd')
    elif i == 3:
        print(str(i) + 'rd')
    else:
        print(str(i) + 'th')
