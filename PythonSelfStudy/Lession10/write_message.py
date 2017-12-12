import os
os.listdir()

''' 先获取当前文件的路径 '''
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(THIS_FOLDER, 'programming.txt')

''' 使用w模式打开文件会把文件中的内容先清空 '''
with open(filename,'w') as file_obj:
    file_obj.write('Input into file1.\n')
    file_obj.write('Input into file2.\n')

''' 使用a模式打开文件会保留文件中的内容 '''
with open(filename,'a') as file_obj:
    file_obj.write('Input into with a model.\n')
    file_obj.write('Input into with a model2.\n')