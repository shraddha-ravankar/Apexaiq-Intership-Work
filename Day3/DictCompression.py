""" Traiditional way to create a dictionary"""
squares = {}

for i in range(1, 6):
    squares[i] = i * i

print(squares)


squares = {i: i * i for i in range(1, 6)}
print(squares)


"""Dictionary Compression with list"""
names = ["Alex", "Bob", "Charlie"]

name_length = {name: len(name) for name in names}
print(name_length)


keys = ['a','b','c','d','e']
values = [1, 2, 3, 4, 5]  

d = {k:v for (k,v) in zip(keys, values)}  
print (d)