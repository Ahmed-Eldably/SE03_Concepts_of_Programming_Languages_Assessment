"""
Object-Oriented Programming
Object: a representation of data
"""

music_list = {
    "Pink Floyd": {
        "albums": {
            "The Dark Side Of The Moon" : {
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
            }
        },
        "about": "Pink Floyd are one ofthe most successful and influential rock groups in history.",
        "monthly_listeners": 13970936,
        "followers": 15875527
    }
}

class Album:
    def __init__(self, band_name, album_name):
        self.band_name = band_name
        self.album_name = album_name

    def songs_names(self):
        return list(music_list[self.band_name]["albums"][self.album_name].keys())

    def total_number_of_songs(self):
        number_of_songs =  len(music_list[self.band_name]["albums"][self.album_name].keys())
        return "Total number of songs in the ablum " + self.album_name + " by " + self.band_name + " is " + str(number_of_songs)
    
    def about_band(self):
        return music_list[self.band_name]["about"]


class Song(Album):

    def __init__(self, band_name, album_name, song_name):
        super().__init__(band_name, album_name)
        self.song_name = song_name

    def number_of_plays(self):
        plays = music_list[self.band_name]["albums"][self.album_name][self.song_name]["plays"]
        return "The song " + self.song_name + " by " + self.band_name + " has been played for " + str(plays) + " times."

pink_floyd_album = Album("Pink Floyd", "The Dark Side Of The Moon")
print(pink_floyd_album.songs_names())
print(pink_floyd_album.total_number_of_songs())
print(pink_floyd_album.about_band())

pink_floyd_song = Song("Pink Floyd", "The Dark Side Of The Moon", "Speak To Me")
print(pink_floyd_song.number_of_plays())
print(pink_floyd_song.about_band())


