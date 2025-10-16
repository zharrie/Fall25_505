from song import Song
from album import Album
from artist import Artist
from playlist import Playlist
from library import MusicLibrary

# Create the library
lib = MusicLibrary()

# Add songs
s1 = Song("Love It If We Made It", "The 1975", 247)   # 4:07
s2 = Song("Somebody Else", "The 1975", 284)           # 4:44
s3 = Song("The Sound", "The 1975", 226)               # 3:46
s4 = Song("If You're Too Shy (Let Me Know)", "The 1975", 222)  # 3:42
s5 = Song("It's Not Living (If It's Not With You)", "The 1975", 242)  # 4:02


for s in [s1, s2, s3, s4, s5]:
    lib.add_song(s)

# Add albums
album1 = Album("I like it when you Sleep", "The 1975"); album1.add_song(s2)
album2 = Album("Notes on a Conditional Form", "The 1975"); album2.add_song(s4)
lib.add_album(album1)
lib.add_album(album2)

# Add playlists
playlist = Playlist("The 1975 Favorites"); playlist.add_song(s1); playlist.add_song(s4); playlist.add_song(s3)
lib.add_playlist(playlist)

def show_playlists(self):
        print("\n --- Playlists ---")
        print(Playlist)

# Display summary
lib.summary()

# Generate statistics
lib.most_played_songs()
lib.longest_songs()
lib.songs_per_artist()
lib.albums_per_artist() == 2
lib.total_library_duration()


# Search and sort
lib.search_songs(artist="The 1975")
lib.sort_songs(by="play_count", reverse=True)

# Save and load
lib.save_to_file("my_library.json")
new_lib = MusicLibrary()
new_lib.load_from_file("my_library.json")

print("\n--- Save Library ---")
lib.save_to_file("my_library.json")

