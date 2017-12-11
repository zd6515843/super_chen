# 导入整个模块
# import lession08_function02

# 导入特定的函数
# from lession08_function02 import build_info22,build_info00

# 使用as给函数指定别名
from lession08_function02 import build_info as bi

# 使用as给模块指定别名
import lession08_function02 as lf2

# 导入模块中所有函数
from lession08_function02 import *

# print(lession08_function02.build_info('andy','zhang',age='3?',height='176'))
# print(build_info22('andy','zhang',age='3?',height='176'))
# print(bi('andy','zhang',age='3?',height='176'))
# print(lf2.build_info('andy','zhang',age='3?',height='176'))

print(build_info00('andy','zhang',age='3?',height='176'))
