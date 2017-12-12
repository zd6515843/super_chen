import os
import json

''' 先获取当前文件的路径 '''
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
test10_1 = os.path.join(THIS_FOLDER, 'learn_python.txt')


print('\n课后练习10-1')
print('\n读取整个文件')
with open(test10_1) as file_obj:
    contents = file_obj.read()
    print(contents.strip())

print('\n遍历文件对象')
with open(test10_1) as file_obj:
    for line in file_obj:
        print(line.strip())

print('\n文件按行存入列表')
with open(test10_1) as file_obj:
    lines = file_obj.readlines()
print(lines)
for line in lines:
    print(line.strip())

print('\n课后练习10-2')
print('\nReplace "python" to "C"')
for line in lines:
    print(line.replace('python','C').strip())

print('\n课后练习10-3')
username = os.path.join(THIS_FOLDER, 'username.txt')
name = input("Please input your user id: ")
with open(username,'a') as file_obj:
    file_obj.write(name+'\n')

print('\n课后练习10-4')
username = os.path.join(THIS_FOLDER, 'whileNames.txt')
while True:
    name = input("Please input your user id: ")
    if name == 'q':
        break
    with open(username,'a') as file_obj:
        file_obj.write(name+'\n')

''' print('\n课后练习10-11')
number = input("Please input your favorite number: ")
save_number = os.path.join(THIS_FOLDER, 'save_number.json')
with open(save_number,'w') as obj:
    json.dump(number,obj)
with open(save_number) as obj:
    num = json.load(obj)
    print("Your favorite number is: " + num) '''

print('\n课后练习10-12')
save_number = os.path.join(THIS_FOLDER, 'save_number.json')
try:
    with open(save_number) as obj:
        num = json.load(obj)
        print("Your favorite number is: " + num)
except FileNotFoundError:
    number = input("Please input your favorite number: ")
    with open(save_number,'w') as obj:
        json.dump(number,obj)