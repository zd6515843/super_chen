# 列表 list []
sports = ['football', 'pingpang', 'swim', 'run']
print(sports)  # ['football', 'pingpang', 'swim', 'run']

print(sports[0]) # football

print(sports[0].title()) # Football

# print(sports[4])   IndexError: list index out of range

print(sports[-1]) # return the last item from this list: 'run'
print(sports[-2]) # 'swim'



# update list
print('\n\n# Update list Start')
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)      # ['honda', 'yamaha', 'suzuki']
motorcycles[0]='ducati' 
print(motorcycles)      # ['ducati', 'yamaha', 'suzuki']

# add to list - at last
print('\n\n# Add to list Start')
motorcycles.append('add1')
print(motorcycles)      # ['ducati', 'yamaha', 'suzuki', 'add1']

test = []
test.append('test1')
test.append('test2')
test.append('test3')
print(test)  # ['test1', 'test2', 'test3']

# add to list with index
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.insert(0,'ducati')	# ['honda', 'yamaha', 'suzuki']
print(motorcycles)				# ['ducati', 'honda', 'yamaha', 'suzuki']
motorcycles.insert(-1,'aaa')	
print(motorcycles)				# ['ducati', 'honda', 'yamaha', 'aaa', 'suzuki']

# del from list
print('\n\n# Delete from list')
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)  # ['yamaha', 'suzuki']

# pop()
print('\n\n# list with pop()')

motorcycles = ['honda','yamaha','suzuki']

pop_motorcycles = motorcycles.pop()
print(motorcycles)	   # ['honda', 'yamaha']
print(pop_motorcycles) # suzuki

motorcycles = ['honda','yamaha','suzuki']
pop_motorcycles = motorcycles.pop(1)
print(motorcycles)	   # ['honda', 'suzuki']
print(pop_motorcycles) # yamaha


# list with remove
print('\n\n# list with pop()')
motorcycles = ['honda','yamaha','suzuki','yamaha']
motorcycles.remove('yamaha')
print(motorcycles)	# ['honda', 'suzuki', 'yamaha']  just remove the first 'yamaha'


# list.sort()
print('\n\n# sort list')
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)	 # ['audi', 'bmw', 'subaru', 'toyota']

cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse = True)
print(cars)  # ['toyota', 'subaru', 'bmw', 'audi']


# sorted(list)
print('\n\n# sorted list')
cars = ['bmw','audi','toyota','subaru']

print(sorted(cars)) # ['audi', 'bmw', 'subaru', 'toyota']
print(cars)			# ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars,reverse = True)) # ['toyota', 'subaru', 'bmw', 'audi']

# list.reverse()
print('\n\n# list.reverse()')
cars = ['bmw','audi','toyota','subaru']
cars.reverse()
print(cars)	#['subaru', 'toyota', 'audi', 'bmw']

# len(list)
print('\n\n# len(list)')
cars = ['bmw','audi','toyota','subaru']
print(len(cars)) # 4


# test 3-8
print('\n\n# Test of 3-8')
places = []
places.append('america')
places.append('japan')
places.append('hainan')
places.append('dali')
places.append('germany')
print('\nplaces is:')
print(places)
print('\nsorted places is:')
print(sorted(places))
print('\nplaces is:')
print(places)
print('\nsorted reverse places is:')
print(sorted(places,reverse=True))

print('\nplaces again:')
print(places)

places.reverse();
print('\nplaces.reverse():')
print(places)

places.reverse();
print('\nplaces.reverse() again:')
print(places)

places.sort();
print('\nplaces.sort():')
print(places)

places.sort(reverse = True)
print('\nplaces.sort(reverse = True):')
print(places)
print(len(places))

