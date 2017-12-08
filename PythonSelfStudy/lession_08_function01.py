
#


def greet_user(name):
    print('Fist function() is: ' + name)


print('\n# 函数')
greet_user('test')

print('\n# 位置实参')


def describe_pet(animal_type, pet_name):
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('dog', 'Vise')
describe_pet('cat', 'miao')

print("\n# 关键字实参 describe_pet(animal_type='dog', pet_name='Vise')")
print("# 关键字实参 describe_pet(pet_name='Vise' ,animal_type='dog')")
describe_pet(animal_type='dog', pet_name='Vise')
describe_pet(pet_name='Vise', animal_type='dog')

print('\n# 默认值, 必须先列出没有默认值的实参')
print("# def describe_pet(pet_name, animal_type ='dog')")


def describe_pet(pet_name, animal_type='dog'):
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(pet_name='Vise')
describe_pet(pet_name='go', animal_type='cat')


print('\n# 8-5')


def describe_city(city, country='China'):
    print(city + " is belong to " + country)


describe_city('Dalian')
describe_city(city='ShenYang')
describe_city('Tokyo', 'Japan')


def get_formatted_name(first, last):
    full_name = first + " " + last
    return full_name.title()


person_info = get_formatted_name('andy', 'zhang')
print(person_info)

print("\n# 让实参为可选 def get_formatted_name(first, last, middle='')")


def get_formatted_name(first, last, middle=''):
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " " + last
    return full_name.title()


person_info = get_formatted_name('andy', 'li')
person2_info = get_formatted_name('andy', 'li', 'mid')
print(person_info)
print(person2_info)

print("\n# 返回字典")


def build_name(first, last, age=''):
    person = {'firstName': first, 'lastName': last}
    if age:
        person['age'] = age
    return person


person = build_name('andy', 'zhang')
person2 = build_name('xx', 'tt', '22')
print(person)
print(person2)


print("\n# Test 8-6")
def city_country(city, country):
    return city.title() + ", " + country.title()
while True:
    print('Quit with "q".')
    iCity = input('City name please: ')
    if iCity =='q':
        break
    iCountry = input('Country name plesae: ')
    if iCountry =='q':
        break
    print(city_country(iCity,iCountry))

print("\n# Test 8-7")
def make_song_list(singer, songName, numb = ''):
    song_list = {'Singer':singer,'Song':songName}
    if numb:
        song_list['Num'] = numb
    return song_list
print(make_song_list('Sunyanz','MyLove','10'))
print(make_song_list('Xinzhe','XinYang'))

print("\n# Test 8-8")
def build_song_list(singer, songName):
    song_list = {'Singer':singer,'Song':songName}
    return song_list
while True:
    song_list={}
    print('Enter "q" to quit.')
    iSinger = input('Singer name please: ')
    if iSinger =='q':
        break
    iSongName = input('songName name plesae: ')
    if iSongName =='q':
        break
    song_list = build_song_list(iSinger,iSongName)
    print(song_list)

print("# 8.4 传递列表")
def print_names(names):
    for name in names:
        print("User name is " + name)

user_names = ['梅西','C 罗','法尔考']
print_names(user_names)

print("\n# Test 8-11")
def print_list(list):
    for member in list:
        # print(str(member).title + " is a great Migic player.")
        print(member.title())

def copy_list(existList, targetList):
    while existList:
        member = existList.pop()
        targetList.append(member)

existList = ['zacard', 'moon', 'Lucifa']
targetList=[]
copy_list(existList[:], targetList)
print_list(targetList)
print_list(existList)

print("\n# 8.5 传递任意数量的实参")
def languages(*list):
    for member in list:
        print(member + " is my choice")
    print('0000')
languages()
languages('java','python','js')

def make_pizza(size, *toppings):
    print('\nMakeing a '+str(size) + ' pizza'
    + ' with the following toppings:')
    for topping in toppings:
        print("-" + topping)
make_pizza(12)
make_pizza(13,'cong','jiang')

print("\n# 8.5.2 使用任意数量的关键字实参 def build_info(firstName, lastName, **userInfo):")
print("# build_info('andy','zhang',age='3?',height='176')")
def build_info(firstName, lastName, **userInfo):
    info ={}
    info['FirstName']= firstName
    info['LastName']= lastName
    for key,value in userInfo.items():
        info[key] = value
    return info
print(build_info('andy','zhang',age='3?',height='176'))

