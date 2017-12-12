import json
import os

''' 先获取当前文件的路径 '''
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(THIS_FOLDER, 'number.json')

with open(filename) as obj:
    numbers = json.load(obj)
print(numbers)