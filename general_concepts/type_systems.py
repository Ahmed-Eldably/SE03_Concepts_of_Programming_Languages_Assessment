"""
Type systems: Progrmming languages have a type system that formalizes which categories of objects it can work with and how these catagories are treated.
"""

# Python is a dynamic typed language. In a dynamic language, the interpreter checks the type only as the code runs. It also allows
# to the typeof variable to change over its lifetime.

best_band = "Pink Floyd"
total_number_of_pink_floyd_albums = 15

if False:
    result = best_band + total_number_of_pink_floyd_albums # this line will never run, so no type error will be raised
else:
    print(best_band + str(total_number_of_pink_floyd_albums))

#print(best_band + total_number_of_pink_floyd_albums) # This one will be checked and will raise a type error.

# type of a variable can be changed over time
total_number_of_pink_floyd_albums = 15
print(type(total_number_of_pink_floyd_albums))

total_number_of_pink_floyd_albums = "15"
print(type(total_number_of_pink_floyd_albums))

"""
In static typing, checks are performed without running the program. This happens in languages like C and Java.
String band_name
band_name = "Pink Floyd"

As first line declares that the first variable is string. This is someting that can not be changed in the future.
It can never be assigned to a value that's not a sting
"""

"""
Duck typing: "if it walks like a duck and it quacks like a duck, then it must be a duck"
It is a concept related to dynamic typing, where the type of the class of an object is less importaant than the methods it define.
They only check for the presence of a given method or attribute.
"""

class PinkFloydAlbums:
    def __len__(self):
        return 15

pink_floyd_albums = PinkFloydAlbums()
print(pink_floyd_albums)
print(len(pink_floyd_albums))

"""
Gradual Typing
- A.k.a. optional static typing.
- Best of both worlds  (?)
    - some code can be dynamically typed.
    - some code can statically typed.
- A path to static typing for a large dynamic code base.
    - gradually introduce typing.
    - start wit most commonly used modules.
- Also known from e.g. TypeScript (JS) and Hack (PHP)
"""
def len_albums_for_band(total_number_of_albums: str, band_name: str) -> str:
    return band_name + " has made " + total_number_of_albums + " albums."

print(len_albums_for_band(15, "Pink Floyd"))