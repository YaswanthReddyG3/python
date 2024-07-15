## Types - int, float, list, dict, tuple

# Lists

# Basic definition

my_list = []

my_list = [1,2,3,"alpha",[4,5,6]] # List can contain any type of items, ex: list can contains another list.and

# print(my_list[4][2])

# Append

my_list = []
my_list.append(3)

new_list = ['a','b','c','b','b','c']
my_list.extend(new_list)
my_list.append(['d','e'])
# my_list.clear()
# print(my_list) # 3,a,b,c,[d,e]

my_list.pop()
my_list.insert(2,"g3")

new_list = my_list.copy()
my_list.pop()
print(my_list.count('b'))
print(my_list)
print(my_list.index('c'))
my_list.remove('b')
# my_list.reverse()

from functools import cmp_to_key
def comp(a,b):
    if str(a) > str(b):
        return -1
    elif str(a) < str(b):
        return 1
    else:
        return 0

# my_list.sort(key=cmp_to_key(comp))

print(my_list)

print(my_list[2:6:2])

