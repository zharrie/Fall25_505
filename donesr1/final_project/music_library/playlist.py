from song import Song

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
            print(f"Added '{song.title}' to playlist '{self.name}'")
        else:
            print(f"'{song.title}' is already in playlist '{self.name}'")

    def __str__(self):
        if not self.songs:
            return f"Playlist '{self.name}' is empty."
        song_list = "\n".join([f"  - {s.title} by {s.artist}" for s in self.songs])
        return f"Playlist: {self.name}\n{song_list}"
