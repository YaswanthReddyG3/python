# Type: Dictionary and other basic types

# Dictionary: Contains key - values. Keys should be immutable and hashable

my_dict = {}
my_dict = {'key': 'value', 2: [1, 2, 3], 3: {3: 'k', 4: {5:'y'}}}

#print(my_dict[3][4][5])
# my_dict.clear()
#my_dict.pop('key')
# my_dict['new_key'] = 'new value'
# my_dict.copy()
new_dict = my_dict.copy()
my_dict['key']= 'new value'

print(my_dict.get(5))

print(dict.fromkeys([1,2,3,3],[3,4,5]))

# below code does same thing as dict.fromkeys(), showed it for learning and comparison purpose
# for i in range(0,6):
#     my_dict[keys_list[i]]="value"

print(my_dict.items())

# for key, value in my_dict.items():
#     print(value)

print(my_dict.keys())


print(my_dict.setdefault('random','dream'))
my_dict.update({'random':'new dream'})
print(my_dict)