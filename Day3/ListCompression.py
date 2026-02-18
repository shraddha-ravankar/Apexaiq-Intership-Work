"""
ListCompression
"""
marks = [45, 67, 89, 34]

passed = [m for m in marks if m >= 50]
print(passed)


"""List Compression with Strings
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


"""List Compression with Range"""
numbers=[ i for i in range(100) if i%2!=0]
print(numbers)