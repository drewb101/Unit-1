my_dictionary = {"key": "Hello", "key2": "World!"}

# what happens if we comment out the line below?
#my_dictionary['key'] = 'value'

#print(my_dictionary)

#del my_dictionary['key']
my_dictionary.pop('key', None)

print(my_dictionary)
