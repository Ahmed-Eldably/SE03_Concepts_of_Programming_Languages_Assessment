"""
Variable: a label given to a certain location in memory. T
DType: In most programming languages, you have to set the data type of the variable (int, float, string, etc)

rules to set a variable:
* It has to contain only letters(uppercase or lowercase), numbers or the underscore charcter.
* It may not start with a number.
* It may not be a reseved keyword
"""

# Variable scope: the part that is accessible from the code. LEGB rule (local -> Enclosing -> Global -> Built-in)

# 1. Local Scope: a variable within a function, its scope lies only within the function.

def pink_floyd_best_album():

    best_album = "The Dark Side of the Moon"

    # first print statment
    print(best_album)

pink_floyd_best_album()

#print(best_album)

# 2. Enclosing Scope: the outer's variable have a larger scope and can be accessed from the enclossed inner function.

def pink_floyd_best_album(): # outter function
    best_album = "The Dark Side of the Moon"

    def best_song_of_the_album(): # inner function
        best_song = "Time"

        # first print statement in the inner scope
        print("best album from the outer function", best_album)

        # second print statement in the inner scope
        print("Best song from the inner function", best_song)

    best_song_of_the_album()
    # third print statement in the outter scope
    #print("Best song from the inner function", best_song)

pink_floyd_best_album()

# 3. Global Scope: the variable is defined outside of any function, and can be accessed through all functions used.

band_name = "Pink Floyd"

def pink_floyd_best_album():
    best_album = "The Dark Side of the Moon"
    print("The best album of {} is {}.".format(band_name, best_album))

def best_song_of_the_band():
    best_song = "Time"
    print("The best song of {} is {}.".format(band_name, best_song))

pink_floyd_best_album()
best_song_of_the_band()

# 4. Built-in Scope: the widest scope in any language that has all the reserved words in the language. It can be accessed any where in te code.
print(True, False, int, float, str)
