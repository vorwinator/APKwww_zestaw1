print('Liczę sobie {0}, {1}, {2}.'.format("raz", "dwa", "trzy"))
print('Liczę sobie {0}, {1}, {2}.'.format("1", "2", "3"))
print('Liczę sobie {1}, {2}, {0}.'.format("1", "2", "3"))
class Data(object):
    def __str__(self):
        return 'str'
    def __repr__(self):
        return 'repr'
print('Liczę sobie {0!s}, {0!r}.'.format(Data()))
class Data2(object):
    def __repr__(self):
        return 'räpr'
print('Liczę sobie {0!r}, {0!a}.'.format(Data2()))
print('{:>10}'.format('test'))
print('{:10}'.format('test'))
print('{:_<10}'.format('test'))
print('{:^10}'.format('test'))
print('{:^6}'.format('zip'))
print('{:.5}'.format('xylophone'))
print('{:10.5}'.format('xylophone'))
print('{:f}'.format(3.141592653589793))
print('{:04d}'.format(42))
print('{: d}'.format((- 23)))
data = {'first': 'Hodor', 'last': 'Hodor!'}
print('{first} {last}'.format(**data))
from datetime import datetime
print('{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5)))
