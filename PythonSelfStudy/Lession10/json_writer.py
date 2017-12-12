import json
import os

numbers = [2, 3, 5, 7, 11, 13]

''' 先获取当前文件的路径 '''
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(THIS_FOLDER, 'number.json')

with open(filename,'w') as obj:
    json.dump(numbers,obj)