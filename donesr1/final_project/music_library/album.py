from song import MusicItem, Song

class Album(MusicItem):
    def __init__(self, title, artist, year=None, genre=None):
        super().__init__(title, year, genre)
        self.artist = artist
        self.songs = []

    def add_song(self, song):
        if isinstance(song, Song):
            self.songs.append(song)
        else:
            raise TypeError("Can only add Song objects to Album.")

    def total_duration(self):
        return sum((song.duration for song in self.songs), start=0)

    def __str__(self):
        return f"Album: {self.title} by {self.artist} ({len(self.songs)} songs)"
