from playlist import Playlist
from song import Song

"""Problem Description: Create a music library manager that organizes songs, creates
                        playlists, and provides search functionality."""
"""Save library data to files (consider JSON format)"""

class MusicLibrary:
    def __init__(self, library_name):
        self.library_name = library_name
        self.playlists = {}

    def create_playlist(self, playlist_name, list_of_songs_to_add_to_playlist):
        new_playlist = Playlist(playlist_name)
        new_playlist.add_songs(list_of_songs_to_add_to_playlist)
        self.playlists[playlist_name] = new_playlist

    def sort_by(self, playlist_name, key):
        self.playlists[playlist_name].sort(key)        
        
    def search(self, playlist_name, key, value_to_search):
        self.playlists[playlist_name].search(key, value_to_search)

    def print_statistics(self, playlist_name, key):
        self.playlists[playlist_name].print_statistics(key)

    def save_playlist_to_json(self, playlist_name):
        self.playlists[playlist_name].save_to_json()


if __name__ == "__main__":


  s1 = Song(title='In the End', genre='Nu Metal', duration=216, year=2000, file_format='mp3', artist='Linkin Park', album='Hybrid Theory')
  s1.increment_play_count(213)
  s2 = Song(title='Numb', genre='Nu Metal', duration=186, year=2003, artist='Linkin Park') #Single w/o Album
  s2.increment_play_count(500)
  s3 = Song(title='Lithium', genre='Gothic Rock', duration=224, year=2006, artist='Evanescence', album='The Open Door')
  s3.increment_play_count(478)
  s4 = Song(title='Aluminium', genre='Fake-Pop', duration=333, year=2077, file_format='docx', artist='NotFakeBand', album='IDK') # wrong file format


  m = MusicLibrary('My Library')
  m.create_playlist('LP Hits', [s1, s2])
  m.create_playlist('LP Hits2', [s1, s2, s2]) # Duplicate Song
  m.create_playlist('Favs', [s3, s1, s2])

  m.sort_by('Favs', 'title')
  m.sort_by('Favs', 'artist')
  m.sort_by('Favs', 'album')
  m.sort_by('Favs', 'duration')
  m.sort_by('Favs', 'play_count')

  m.search('Favs', key='artist', value_to_search='Linkin Park')
  m.search('Favs', 'album', 'The Open Door')
  m.search('Favs', 'genre', 'Nu Metal')
  m.search('Favs', 'year', 2003)



  m.print_statistics('Favs', 'most_played')
  m.print_statistics('Favs', 'longest_songs')
  m.print_statistics('Favs', 'overall_stats')


  m.save_playlist_to_json('Favs')
 