from artist import Artist
from album import Album

class InvalidFileFormat(Exception):
    def __init__(self, value):
        self.value = value



class Song(Artist, Album):
    def __init__(self, title, genre, duration, year, file_format='mp3', artist = "", album = ""):
        Artist.__init__(self, artist)
        Album.__init__(self, album)
        self.title = title
        self.genre = genre
        self.duration = duration
        self.year = year
        self.play_count = 0

        self.valid_file_formats = ['mp3', 'wav']

        #Implement exceptions for invalid file formats
        try:
            if file_format in self.valid_file_formats:
                self.file_format = file_format
            else:
                raise InvalidFileFormat(f'Format should be one of {self.valid_file_formats}')
        except InvalidFileFormat as e:
            print(e)
        

    def increment_play_count(self, n=1):
        self.play_count += n

