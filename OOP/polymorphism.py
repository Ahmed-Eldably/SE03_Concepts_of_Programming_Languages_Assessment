"""
Polymorphism: the condition of occurrence in different forms.
"""

# example1: Polymorphism in aaddition operator

# you can use it to sum two numbers
pink_floyd_albums = 15
led_zeppelin_albums = 8
print(pink_floyd_albums + led_zeppelin_albums)

# you can also use itto concatenate two variables
band = "Pink Floyd"
music = "rock"

print(band + " is a " + music + " band.")

"""
Function polymorphism: Python has some functions that are compatible to run with multiple data types.
The len() function is an example of that.
"""

# example 2: Polymorphic len() function

print(len("Pink Floyd"))
print(len(["Pink Floyd", "Led Zeppelin", "The Beatles", 'Radiohead']))
print(len({"band":"Pink Floyd", "Music": "Rock"}))

"""
Class Polymorphism: The concept of polymorphism is used while creating class methods.
Python allows different classes to ave methods with the same name. 
"""

# example 3: Polymorphism in class methods.
class Album:
    def __init__(self, name) -> None:
        self.name = name

    def about(self):
        return f"{self.name} is the eleventh studio album by the English rock band the Beatles, released on 26 September 1969 by Apple Records."

    def plays(self) -> float:
        return 1800000000

class Song:

    def __init__(self, name) -> None:
        self.name = name

    def about(self):
        return f"\"{self.name}\" is a song by the English rock band the Beatles from their 1969 album Abbey Road. It was written by George Harrison, the band's lead guitarist."

    def plays(self) -> float:
        return 79364896

album1 = Album("Abbey Road")
song1 = Song("Something")

for music_piece in (album1, song1):
    print(music_piece.name)
    print(music_piece.about())
    print(music_piece.plays())

"""
Polymorphism and inheritance

We can redefine certain methods and attributes specifically to fit the child class, which is know as method overroding.

Polymorphism allows to access these overriden methods and attributes that have the same name as the parent class.
"""

# example 4: Method Overriding
class Artist:

    def __init__(self, name) -> None:
        self.name = name

    def about(self):
        return "Radiohead are an English rock band formed in Abingdon, Oxfordshire, in 1985. The band consists of Thom Yorke, brothers Jonny Greenwood and Colin Greenwood, Ed O'Brien and Philip Selway. They have worked with producer Nigel Godrich and cover artist Stanley Donwood since 1994."

    def __str__(self) -> str:
        return self.name

    
class Album(Artist):

    def __init__(self, album_name) -> None:
        super().__init__(album_name)
        

    def about(self):
        return "OK Computer is the third studio album by English rock band Radiohead, released on 21 May 1997 on EMI subsidiaries Parlophone and Capitol Records. Radiohead self-produced the album with Nigel Godrich, an arrangement they have used for their subsequent albums."

class Song(Artist):

    def __init__(self, song_name) -> None:
        super().__init__(song_name)

    def about(self):
        return "\"Karma Police\" is a song by the English alternative rock band Radiohead, released as the second single from their third studio album OK Computer (1997) on 25 August 1997."

album1 = Album("Ok Computer")
song1 = Song("Karma Police")

print(album1)
print(song1)

print(album1.about())
print(song1.about())



# References: https://www.programiz.com/python-programming/polymorphism