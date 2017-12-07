#
print('\n#Test 7-10 度假')
name_place={}
flag=True
while flag:
    name = input('Your name please: ')
    place = input('Your dream place to go: ')
    next = input('Any other wishes? yes/no: ')
    name_place[name] = place
    if next == 'no':
        flag = False
print(name_place)
print('# End #\n\n\n')

print('\n#Test 7-8/9 熟食店')
list_meat = ['猪肉','牛肉','猪肉','羊肉','猪肉','鸡肉',]
list_fish = []
while list_meat:
    fish = list_meat.pop()
    print(fish)
    list_fish.append(fish)
print(list_fish)

list_meat = ['猪肉','牛肉','猪肉','羊肉','猪肉','鸡肉',]
list_fish = []
while '猪肉' in list_meat:
    print(list_meat)
    list_meat.remove('猪肉')
finish = list_meat[:]
print('finish')
print(finish)

print('# End #\n\n\n')




response={}
goOn = True
while goOn:
    name = input('What your name is: ')
    where = input('where you want to go: ')
    response[name] = where
    repeat = input('Keep on going : yes or no ')
    if repeat == 'no':
        goOn = False
print(response)
print('# End #\n\n\n')

pets = ['cat', 'dog','cat', 'dog1','cat', 'dog2']
while 'cat' in pets:
    pets.remove('cat')
    print(pets)


unconfirm_user = ['a','b','d','x']
confirm_user=[]
while unconfirm_user:
    print('unconfirm_user')
    print(unconfirm_user)
    user = unconfirm_user.pop()
    confirm_user.append(user)
    print('confirm_user')
    print(confirm_user)

print('\n#Test 7-5 电影票')
while True:
    age = input('Input your age please: ')
    if age != 'quit' and int(age) < 3:
        print('You are free')
    elif age != 'quit' and int(age) < 12:
        print('You need pay $10')
    elif age != 'quit' and int(age) >= 12:
        print('You need pay $15')
    elif age != 'quit':
        print('Input again')
    elif age == 'quit':
        print('See you next time')
        break



while True:
    city = input('Input something until quit: ')
    if city == 'quit':
        break
    else:
        print('I want to go to: ' + city)

mes = "Tell me something, and enter 'quit to end the program'\n"
inputInfo = ""
while inputInfo != 'quit':
    inputInfo = input(mes)
    print(inputInfo)


print('\n#while')
number = 1
while number <= 5:
    print(number)
    number = number + 1


# input()
message = input("Tell me something and i will repeat it back to you: \n")
print('Your inpyt is: ' + message)

num = input("Enter a number and will tell you if it's even or odd: ")
num = int(num)
if num % 2 == 0:
    print('\nThe number ' + str(num) + ' is even.')
else:
    print('\nThe number ' + str(num) + ' is odd.')

# 提示用户输入 python2.7 中用 raw_input()

print('\nTest 7-1 租车')
car = input('Which car you want: \n')
print('Let me see if i can find a ' + car.title() + ' for you.')

print('\nTest 7-2 餐馆订位')
num = input('How many people will come to have dinner: \n')
if int(num) > 8:
    print('There is not enough space for you.')
else:
    print('Ok, we have booked one room for you.')

print('\nTest 7-3 10的整数倍')
num = input("Input a number and will tell you if it's 10 倍数: \n")
if int(num) % 10 == 0:
    print(str(num) + ' is 10的倍数')
else:
    print(str(num) + ' is not 10的倍数')
