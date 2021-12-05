"""
Object-Oriented Programming
Object: a representation of data
"""

music_list = {
    "Pink Floyd": {
        "albums": {
            "The Dark Side Of The Moon" : {
                "songs" : {
                    "Speak To Me" : {
                        "artist" : "Pink Floyd",
                        "plays" : 63986712,
                        "duration": 64,
                        "about_artist": "Pink Floyd are one ofthe most successful and influential rock groups in history."
                    },
                    "Breathe (In the Air)" : {
                    },
                    "On The Run": {
                    },
                    "Time": {
                        "artist" : "Pink Floyd",
                        "plays" : 214737396,
                        "duration": 422,
                        "about_artist": "Pink Floyd are one ofthe most successful and influential rock groups in history."
                    },
                    "The Great Gig In The Sky": {
                    },
                    "Money": {
                    },
                    "Us And Them": {
                    },
                    "Any Colour You like":{
                    },
                    "Brain Damage":{
                    },
                    "Eclipse":{
                    }
                },
                "album_rank" : None
            }
        },
        "about": "Pink Floyd are one ofthe most successful and influential rock groups in history.",
        "monthly_listeners": 13970936,
        "followers": 15875527
    }
}

class Album(object):
    def __init__(self, band_name, album_name):
        self.band_name = band_name
        self.album_name = album_name
        
    # Getters
    def get_songs_names(self):
        return list(music_list[self.band_name]["albums"][self.album_name]["songs"].keys())

    def get_total_number_of_songs(self):
        number_of_songs =  len(music_list[self.band_name]["albums"][self.album_name].keys())
        return "Total number of songs in the ablum " + self.album_name + " by " + self.band_name + " is " + str(number_of_songs)
    
    def get_about_band(self):
        return music_list[self.band_name]["about"]

    # setters
    def set_album_rank(self, rank):
        self.rank = rank
        return self.rank

    def __str__(self) -> str:
        return "Band: " + str(self.band_name) + ", Album: " + str(self.album_name)

class Song(Album):
    tag = 1
    def __init__(self, band_name, album_name, song_name):
        super().__init__(band_name, album_name)
        self.song_name = song_name
        self.id = Song.tag
        Song.tag += 1
        
    # getters
    def get_number_of_plays(self):
        plays = music_list[self.band_name]["albums"][self.album_name]["songs"][self.song_name]["plays"]
        return "The song " + self.song_name + " by " + self.band_name + " has been played for " + str(plays) + " times."
    
    # setters
    def set_plays(self, new_plays):
        plays = music_list[self.band_name]["albums"][self.album_name]["songs"][self.song_name]["plays"] 
        plays += new_plays
        return plays
    # override
    def __str__(self) -> str:
        return "Band: " + str(self.band_name) + ", Album: " + str(self.album_name) + ", Song: " + str(self.song_name)

pink_floyd_album = Album("Pink Floyd", "The Dark Side Of The Moon")
print(pink_floyd_album.get_songs_names())
print(pink_floyd_album.get_total_number_of_songs())
print(pink_floyd_album.get_about_band())
print(pink_floyd_album.set_album_rank('5th'))
print(pink_floyd_album)
print("\n")

song1 = Song("Pink Floyd", "The Dark Side Of The Moon", "Speak To Me")
print(song1.get_number_of_plays())
print(song1.get_about_band())
print(song1.set_plays(5))
print(song1.id)

song2 = Song("Pink Floyd", "The Dark Side Of The Moon", "Time")
print(song2.id)




