
magics = ['fire', 'ice', 'wind']
for magic in magics:
    print('Magic @ : ' + magic)
print('enemy down!')
print('enemy 22 down!\n')

# test 4-1
foods = ['jiaozi', 'haixian', 'kaorou']
for food in foods:
    print('\tI like: ' + food)
print('And i like jiaozi most\n')

# range()
for value in range(1, 5):
    print(value)  # 1~4

numbers = list(range(1, 5))
print('\n\nnumbers is')
print(numbers)

numbers = list(range(1, 16, 5))
print('\n\nlist(range(1,16,5)) is')
print(numbers)  # [1, 6, 11]

numbers = list(range(1, 17, 5))
print('\n\nlist(range(1,17,5)) is')
print(numbers)  # [1, 6, 11, 16]


squares = []
for number in range(1, 11):
    squares.append(number**2)
print('\n\nsquares is')
print(squares)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print('min is ' + str(min(numbers)))
print('max is ' + str(max(numbers)))
print('sum is ' + str(sum(numbers)))

# list 解析
squares = [value**2 for value in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# test 4-3 for 1~20
print('\ntest 4-3')
for num in range(1, 21):
    print(num)

# test 4-4 创建列表1~100
print('\ntest 4-4')
list = []
for num in range(1, 101):
    list.append(num)
print(list)


# test 4-5 创建列表1~100 min max sum
print('\ntest 4-5')
list = []
for num in range(1, 101):
    list.append(num)
print(list)
print(min(list))
print(max(list))
print(sum(list))


# test 4-6 1~20 奇数
print('\ntest 4-6 1~20 奇数')
list = []
for num in range(1, 20, 2):
    print(num)

# test 4-7 3~30 3的倍数
print('\ntest 4-7 3~30 3的倍数')
list = []
for num in range(3, 31, 3):
    print(num)


# test 4-8 1~10 立方 list
print('\ntest 4-8 1~10 立方 list')
list = [value**3 for value in range(1, 11)]
print(list)


# list[0:3]
list = [1, 2, 3, 4, 5]
print('\nlist[0:3]')
print(list[0:3])  # [1, 2, 3]
print(list[1:])  # [2, 3, 4, 5]
print(list[:3])  # [1, 2, 3]
print(list[-2:])  # [4, 5]


plays = ['ronaerdo', 'baqio', 'messi', 'kaka']
for play in plays[:3]:
    print('Football star: ' + play.title())
transferPlays = plays[:]
print('transferPlays is: ')
print(transferPlays)

plays.append('Wulei')
print(plays)
print(transferPlays)

# 元组 不可变
list = (100, 50)
print(list[0])
print(list[1])
# list[0]= 66 TypeError: 'tuple' object does not support item assignment


# test 4-13
foods = ('bread', 'milk', 'meat', 'fruit', 'wine')
for food in foods:
    print('We have ' + food)
#foods[0] = 'banana'
foods = ('bread', 'milk', 'noodle', 'fruit', 'bear')
for food in foods:
    print('We have ' + food)
