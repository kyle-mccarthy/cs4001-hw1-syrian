# the list example, adding items the interating
list_example = []
list_example.append('one value')
list_example.append('another value')
list_example.append('the last value')

# iterate the list
for items in list_example:
    print(items)

# the dict example
dict_example = {}
dict_example['key'] = 'value'
dict_example['another'] = 'item'
dict_example['the final'] = 'value in the list'

# iterate the values
for value in dict_example:
    print(value)

# iterate the keys
for key in dict_example.keys():
    print(key)

