# Higher-order-function map
# map(<f>, <iterable>)

print(list(map(lambda x: x **2, range(2, 5))))

# list comprehension instead of map
print([x**2 for x in range(2, 5)])

# Higher-order-function filter
print(list(filter(lambda x: x > 10, range(1, 14))))

# list comprehension of filter
print([x for x in range(1, 14)if x > 10])

# Decorators - Application of closures

import functools

def decorator(func):
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        print("We have a decorator here")
        return func(*args, **kwargs)
    return new_func

@decorator
def add(a, b):
    return a + b

print(add(4, 5))

# Avoid side effects of OOP

class MyClass(object):

    def __init__(self):
        self.variable1 = self._make_variable1()
        self.variable2 = self._make_variable2()

    @staticmethod
    def _make_variable1():
        var1 = "Pink Floyd"
        return var1

    @staticmethod
    def _make_variable2():
        var2 = "The Beatles"
        return var2

print(MyClass().variable1)

print(MyClass().variable2)

# Frreeze classes - One Liner Version (Keeping things immutable)

class Reader(object):

    def __init__(self) -> None:
        self.lyrics = self._read()

    @staticmethod
    def _read():
        return tuple(tuple(line.split()) for line in open("time_pink_floyd.txt"))


print(Reader().lyrics)





# Stepwise Freezing and Thawing
# Useful in legacy code: Where are data modified?
        #   Complex systems: detect unwanted modification 

class FreezingUnFrozen(object):

    def __init__(self):
        self.__repr = {}
        self.__frozen = False

    def __getitem__(self, key):
        return self.__repr[key]

    def _setitem__(self, key, value):
        if self.__frozen:
            raise KeyError("Key cannot be changed %r"% key)
        self.__repr[key] =value

    def freeze(self):
        self.__frozen = True
    def unfreeze(self):
        self.__frozen = False

    
f = FreezingUnFrozen()
f["a"] = 100
f.freeze()


# references: https://www.youtube.com/watch?v=Ta1bAMOMFOI&list=PLuLuNSvK-OJcy3bv9O8jBvQez08Y9ZMp4&index=1