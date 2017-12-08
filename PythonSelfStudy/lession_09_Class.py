
class Dog():

    def __init__(self, name, age):
        ''' 初始化属性name age '''
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over.")


my_dog = Dog('vis', 5)
print('My dog name is ' + my_dog.name.title())
print('My dog is ' + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()


class Restaurant():
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print("Restaurant name is " + self.name.title())
        print("Restaurant type is " + self.type)

    def open_restaurant(self):
        print("Restaurant " + self.name.title() + " is openning")


restautant_1 = Restaurant('jyj', '盖饭')
restautant_1.describe_restaurant()
restautant_1.open_restaurant()

restautant_2 = Restaurant('kfc', '汉堡')
restautant_3 = Restaurant('一亩三分地', '炒菜')
restautant_2.describe_restaurant()
restautant_3.describe_restaurant()


class Car():
    def __init__(self, name, type, year):
        self.name = name
        self.type = type
        self.year = year
        self.miles = 0

    def get_car_info(self):
        print("Car info: " + self.name.title() +
              " " + self.type + " " + self.year)

    def read_car_miles(self):
        print("Miles of this car is " + str(self.miles))

    def update_miles(self, mile):
        if mile >= self.miles:
            self.miles = mile


my_car = Car('奇骏', '运动版', '2019')
my_car.get_car_info()
my_car.read_car_miles()
my_car.miles = 20
my_car.read_car_miles()

my_car.update_miles(12)
my_car.read_car_miles()

class Life():
    def __init__(self,lifeTime=10):
        self.lifeTime = lifeTime

    def get_life_time(self):
        print("Life time is " + str(self.lifeTime) + " years.")


'''  子类 '''
''' 创建子类时父类必须包含在当前文件中 并且位于子类的前面 '''
class Elic(Car):
    def __init__(self, name, type, year):
        ''' 初始化父类的属性,再初始化电动汽车的属性 '''
        super().__init__(name, type, year)
        self.battery_size = 66
        ''' 将实例用作属性 '''
        self.life = Life()

    def describe_battery(self):
        print("This is a " + str(self.battery_size) + "-kWh battery.")

    ''' 重写父类的方法 get_car_info'''
    def get_car_info(self):
        print("Test over wirte def get_car-info()")


elic_car = Elic('雷克萨斯', '运动版', '2019')
elic_car.get_car_info()
elic_car.describe_battery()
elic_car.get_car_info()
elic_car.life.get_life_time()

'''   导入类的几种方法
  前提条件: car.py 中包含了 类Car() 类ElectricCar() ...

  1.从一个模块中导入一个多个类
    from car import Car, ElectricCar
    my_car = Car(self,..,..)
    my_car2 = ElectricCar(self,..,..)

  2.导入整个模块
    import car
    my_car = car.Car(self,..,..)
    my_car2 = car.ElectricCar(self,..,..)

  3.导入模块中所有的类  不推荐,不知道有哪些类
    from car import *
   '''
