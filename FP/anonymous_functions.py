"""
Anonymous function: a function without an identifier.

Lambda:
* Allows very limited anonymous functions.
* Experssions only, not statments
* Useful callbacks
"""
print((lambda x, y, z: (x + y + z) / 3)(2, 4, 10))