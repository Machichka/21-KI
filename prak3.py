dictionary = {
    'name': 'machichka',
    'age': 17,
    'dict': {'1': 'topchik',
             '2': 'Hello world',
             '3': 2525,
             '4': False,
             '5': True},
    'python': 'piton',
}
print(dictionary)

type_dict = {}
for key, value in dictionary.items():
    if type(value) == dict:
        for key1, value1 in value.items():
            type_dict[key1] = type(value1)
    else:
        type_dict[key] = type(value)
print(type_dict)
