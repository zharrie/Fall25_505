from datetime import timedelta

class MusicItem:
    def __init__(self, title, year=None, genre=None):
        self.title = title
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"{self.title} ({self.year})" if self.year else self.title


class Song(MusicItem):
    def __init__(self, title, artist, duration, year=None, genre=None):
        super().__init__(title, year, genre)
        self.artist = artist  # string or Artist object
        self.duration = timedelta(seconds=duration)
        self.play_count = 0

    def play(self):
        self.play_count += 1

    def __str__(self):
        minutes, seconds = divmod(self.duration.seconds, 60)
        return f"{self.title} by {self.artist} ({minutes}:{seconds:02d}) [{self.play_count} plays]"
