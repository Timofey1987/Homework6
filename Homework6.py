my_dict = {'Daniil': 1987, 'Vera': 1979, 'Sasha': 1997}
print('Dict:', my_dict)
print('Existing value:', my_dict['Vera'])
print('Not existing value:', my_dict.get('Igor'))
my_dict.update({'Igor': 1984, 'Tamara': 1989})
a = my_dict.pop('Sasha')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)


my_set = {8, 4, 4, 4, 3, 'Иркутск', False, (1, 2, 2, 1), 8, 8.64, False, 'Иркутск', True, (1, 2, 2, 3)}
print('Set:', my_set)
my_set.add(8.65)
my_set.add('Хабаровск')
my_set.discard((1, 2, 2, 3))
print('Modified set:', my_set)