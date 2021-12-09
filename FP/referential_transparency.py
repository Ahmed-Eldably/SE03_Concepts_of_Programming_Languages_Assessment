"""
Referential transparency: Expressions can be replaced by its values. 
If we call a function with the same parameters, we know for sure the output will be the same.
"""

def add (a,b):
    return a + b

def substract(a, b):

    return a - b



x = 5
y = 3

print(add(1, 2))
print(add(x, y))
print(add(2, y))
print(add(x, 4))

# Parallelization and ease of debugging
result = add(x, y) + substract(x, y)


# References: https://medium.com/@geisonfgfg/python-functional-programming-8158f736935b