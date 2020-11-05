ls = [34, 'текст', 45.5, True, abs(-7), complex(3, 6), (34, 'test', None), set('abc'),
      {'Paleozoic': 'Dev,Car,Per', 'Mesozoic': 'Tri,Jur,Cre'}]
for el in ls:
    print(f'{el} is {type(el)}')
