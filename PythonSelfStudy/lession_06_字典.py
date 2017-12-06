print('# 列表解析')
list = [value**2 for value in range(1, 4)]
print(list)

print('\n# 字典')
print("alien = {'color': 'green', 'point': 5}'")
alien = {'color': 'green', 'point': 5}
print(alien['color'])
print(alien['point'])

alien['x'] = 0
alien['y'] = 25
print(alien)

if alien:
    print('alien not empty 11')
alien = {}
if alien:
    print('alien not empty 22')

print('\n# 修改字典中的值')
alien = {'color': 'green', 'point': 5}
print(alien['color'])
alien['color'] = 'red'
print(alien['color'])

print('\n# 删除键之对  del')
alien = {'color': 'green', 'point': 5}
del alien['point']
print(alien)

favorite_languages = {
    'fay':'java',
    'andy':'python',
    'nirvana':'js',
    'michele':'java',
}
print(favorite_languages['andy'].title())
print('\n# 字典.items()')
print('for key,value in favorite_languages.items():')
for key, value in favorite_languages.items():
    print('Key is: ' + key + ' value is: ' + value.title())

print('\nfor key in favorite_languages.keys():')
for name in favorite_languages.keys():
    print('Name is: ' + name.title())

print('\nfor key in favorite_languages:')
for name in favorite_languages:
    print('Name is: ' + name.title())

if 'aaa' not in favorite_languages.keys():
    print('There is no aaa in current group')

for name in sorted(favorite_languages):
    print(name.title())

print('\nfor value in favorite_languages.values():')
for name in favorite_languages.values():
    print('Value is: ' + name.title())

print('\nfor value in set(favorite_languages.values()):')
for name in set(favorite_languages.values()):
    print('Value is: ' + name.title())

print('\n#Test 6-5')
footBall = {
    'China':'98',
    'Korea':'30',
    'Japan':'20',
    'Brazil':'5',
}

for country,num in footBall.items():
    print('Number of ' + country + ' is ' + num)

print('\n#country')
for country in footBall:
    print(country)
print('\n#country')
for country in footBall.keys():
    print(country)
print('\n#numbers')
for num in footBall.values():
    print(num)

print('\n#Test 6-6')
newMember = ['Ita','Japan']
for member in newMember:

    if member in footBall.keys():
        print(member + ': welcome to world cup again')
    else:
        print('This is your first time to workld cup: ' + member)



