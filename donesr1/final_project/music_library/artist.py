from album import Album

class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if isinstance(album, Album):
            self.albums.append(album)
        else:
            raise TypeError("Can only add Album objects to Artist.")

    def __str__(self):
        return f"Artist: {self.name} ({len(self.albums)} albums)"
