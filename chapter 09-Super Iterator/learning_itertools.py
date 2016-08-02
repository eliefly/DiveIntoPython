>>> names = list(open('favorite-people.txt'))
>>> names
['Dora\n', 'Ethan\n', 'Wesley\n', 'John\n', 'Anne\n', 'Mike\n', 'Chris\n', 'Sarah\n', 'Ales\n', 'Lizzie']
>>> names = [name.rstrip() for name in names]
>>> names
['Dora', 'Ethan', 'Wesley', 'John', 'Anne', 'Mike', 'Chris', 'Sarah', 'Ales', 'Lizzie']
>>> names = sorted(names)
>>> names
['Ales', 'Anne', 'Chris', 'Dora', 'Ethan', 'John', 'Lizzie', 'Mike', 'Sarah', 'Wesley']

>>> import itertools
>>> groups = itertools.groupby(names, len)
>>> groups
<itertools.groupby object at 0x02A29780>
>>> list(groups)
[(4, <itertools._grouper object at 0x02A205B0>), (5, <itertools._grouper object at 0x02A202F0>), (4, <itertools._grouper object at 0x02A20510>), (5, <itertools._grouper object at 0x02A20530>), (4, <itertools._grouper object at 0x02A205F0>), (6, <itertools._grouper object at 0x02A20930>), (4, <itertools._grouper object at 0x02A208F0>), (5, <itertools._grouper object at 0x02A20910>), (6, <itertools._grouper object at 0x02A208B0>)]






>>> names
['Ales', 'Anne', 'Chris', 'Dora', 'Ethan', 'John', 'Lizzie', 'Mike', 'Sarah', 'Wesley']
>>> names = sorted(names, key=len)
>>> names
['Ales', 'Anne', 'Dora', 'John', 'Mike', 'Chris', 'Ethan', 'Sarah', 'Lizzie', 'Wesley']
>>> groups = itertools.groupby(names, len)
>>> groups
<itertools.groupby object at 0x02A297B0>
>>> list(groups)
[(4, <itertools._grouper object at 0x02A20830>), (5, <itertools._grouper object at 0x02A20590>), (6, <itertools._grouper object at 0x02A20510>)]
>>> list(groups)
[]
>>> groups = itertools.groupby(names, len)
>>> for name_length, name_iter in groups:
    print('Names with {0:d} letters:'.format(name_length))
    for name in name_iter:
        print(name)

        
Names with 4 letters:
Ales
Anne
Dora
John
Mike
Names with 5 letters:
Chris
Ethan
Sarah
Names with 6 letters:
Lizzie
Wesley