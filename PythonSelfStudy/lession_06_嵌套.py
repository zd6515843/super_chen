alien_0 = {'color':'green','point':5}
alien_1 = {'color':'red','point':15}
alien_2 = {'color':'yellow','point':10}
aliens = [alien_0,alien_1,alien_2]
print('# 列表中存字典')
for alien in aliens:
    print(alien)

print('\n# 10个外星人')
aliens=[]
for i in range(10):
    newAlien = {'speed':'slow','color':'green','point':5}
    aliens.append(newAlien)

for alien in aliens:
    print(alien)
print(len(aliens))

print('\n# 改变前3个外星人的属性')
for alien in aliens[:3]:
    alien['color']='yellow'
    alien['speed']='medium'
    alien['point']=10

for alien in aliens:
    print(alien)

print('\n# 字典中存列表````')
print("name_language = {\n'me':['js','python'],\n'fay':['java','js']\n}")

name_language = {
    'me':['js','python'],
    'fay':['java','js'],
    'lool':['java']
}
for name,language in name_language.items():
    print(name)
    for l in language:
        print('\t' + l)

print('\n# 字典中存字典')
users ={
    'Messie':{
        'first':'Zhang',
        'last':'Messie',
        'location':'China'
    },

    'Kaka':{
        'first':'Sheng',
        'last':'kaka',
        'location':'Brazil'
    },
}
users['C_ronarido'] = {
    'first':'Stiyano',
    'last':'C_ronarido',
    'location':'Potora',
}
for name,info in users.items():
    print('\nPlayer name is ' + name)
    print('Player full name is ' + info['first'] + info['last'])
    print('Player is from ' + info['location'])
