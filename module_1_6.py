my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print('Dict: ', my_dict)
print('Existing value: ', my_dict['Masha'])
print('Not existing value: ', my_dict.get('Kamila', 'None' ))
print('Deleted value: ', my_dict['Egor'])
my_dict['Kamila'] = 1981
my_dict['Artem'] = 1915
#print(my_dict)
del my_dict['Egor']
print('Modifiet dictionary: ', my_dict)
my_set = {3, 7, 8, 6.5, 'name', 'surname', 3, 6.5}
print('Set: ', my_set)
my_set.update([1, 2])
my_set.discard('name')
print('Modifiet set: ', my_set)