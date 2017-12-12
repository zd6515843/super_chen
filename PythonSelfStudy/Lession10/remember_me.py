import json
import os

''' 先获取当前文件的路径 '''
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(THIS_FOLDER, 'users.json')

try:
    with open(filename) as obj:
        username = json.load(obj)
except FileNotFoundError:
    with open(filename, 'w') as obj:
        username = input("Please input your name: ")
        json.dump(username, obj)
else:
    print("Welcome back " + username)
