import os
os.listdir()

''' 先获取当前文件的路径 '''
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'pi.txt')
print(my_file)

''' 读取整个文件 '''
print('\n整行读取')
with open(my_file) as file_object:
    contents = file_object.read()
    print(contents)

''' 逐行读取 '''
print('\n逐行读取')
with open(my_file) as file_object:
    for line in file_object:
        print(line.strip())

print('\n绝对路径读取')
with open('C:\\Tool\\Python\\uuu.txt') as file_object:
    contents = file_object.read()
    print(contents)

''' 可以使用上面的方式也可以用下面这种方式: r+'绝对路径' '''
print("\nr+'绝对路径'")
with open(r'C:\Tool\Python\uuu.txt') as file_object:
    contents = file_object.read()
    print(contents)

print("\n文件行存入列表")
with open(r'C:\Tool\Python\projects\Test\Lession10\pi.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
pi_str = ''
for line in lines:
    pi_str +=line.strip()
print(pi_str)
print(len(pi_str))

str = input('Get input from user: ')
print(str)