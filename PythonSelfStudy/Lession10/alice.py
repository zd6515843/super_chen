filename = 'alice.txt'
#     contents = f.read()

try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    # print('The file you are looking for is not there')
    pass
else:
    print(contents)

title = "Alice in Wonderland"
title.split()
print(title.split())
print(len(title.split()))