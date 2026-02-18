""" Traiditional way to create a dictionary"""
squares = {}

for i in range(1, 6):
    squares[i] = i * i

print(squares)

"""Dictionary Compression"""
squares = {i: i * i for i in range(1, 6)}
print(squares)

names = ["Alex", "Bob", "Charlie"]

name_length = {name: len(name) for name in names}
print(name_length)

