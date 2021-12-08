"""
Functional programming: a programming paradigm where programs are constructed by applying and composing functions.
Lisp 1958

Features of FP:
* Everything is a function.
* Immutable data structures.
* Preserve state in functions.
* Recursion instead of loops/iteration

Advantges:
* More robust
* Smaller building blocks
* Better testable
* Focus on algoritmhs (Maths)
* Computational fit with parallel/concurrent programming
* Live updates

Disadvantages
* Different solutions than OOP.
* There's not that much developers using it.
* Doesn't fit for all problems.
* Input/output are side effects.
* Recursion is harder than loops/iteration.
* Immutable data structures may increase run times
"""

"""
Pure functions
"""

def func1():
    return 5

def func2():
    return 2

# everything is still an object
funcs = {"a": func1, "b": func2}
print(funcs["a"]())

print(funcs["b"]())

# Closures

def outer(outer_param):
    def inner(inner_param):
        return outer_param + inner_param
    return inner

func = outer(8)
print(func(5))

print(func.__closure__)

print(func.__closure__[0])

print(func.__closure__[0].cell_contents) # storing state in FP


# Parrtial Functions
import functools

def func(a, b, c):
    return a, b, c

p_func = functools.partial(func, 5) # a is fixed
print(p_func(3, 4))

p_func = functools.partial(func, 5, 3) # a and b are fixed in this 
print(p_func(4))








# References: https://www.youtube.com/watch?v=Ta1bAMOMFOI