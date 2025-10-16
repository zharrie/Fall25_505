import json
import os
from datetime import timedelta
from operator import attrgetter
from song import Song
from album import Album
from artist import Artist
from playlist import Playlist
from exceptions import DuplicateSongError, InvalidFileFormatError

class MusicLibrary:

    def __init__(self):
        self.artists = {}
        self.albums = {}
        self.songs = {}
        self.playlists = {}

    # Add Methods
    def add_artist(self, artist):
        if not isinstance(artist, Artist):
            raise TypeError("Only Artist objects can be added.")
        self.artists[artist.name] = artist

    def add_album(self, album):
        if not isinstance(album, Album):
            raise TypeError("Only Album objects can be added.")
        self.albums[album.title] = album
        if album.artist not in self.artists:
            self.artists[album.artist] = Artist(album.artist)
        self.artists[album.artist].add_album(album)

    def add_song(self, song):
        if not isinstance(song, Song):
            raise TypeError("Only Song objects can be added.")
        if song.title in self.songs:
            raise DuplicateSongError(song.title)
        self.songs[song.title] = song
        if song.artist not in self.artists:
            self.artists[song.artist] = Artist(song.artist)

    def add_playlist(self, playlist):
        if not isinstance(playlist, Playlist):
            raise TypeError("Only Playlist objects can be added.")
        self.playlists[playlist.name] = playlist

    #Search Methods
    def search_songs(self, artist=None, album=None, genre=None, year=None):
        results = list(self.songs.values())
        if artist:
            results = [s for s in results if s.artist.lower() == artist.lower()]
        if album:
            album_obj = self.albums.get(album)
            if album_obj:
                results = [s for s in results if s in album_obj.songs]
            else:
                results = []
        if genre:
            results = [s for s in results if s.genre and s.genre.lower() == genre.lower()]
        if year:
            results = [s for s in results if s.year == year]
        print(f"\n Search results:")
        if results:
            for i, s in enumerate(results, 1):
                print(f"  {i}. {s}")
        else:
            print("No matches found.")
        return results

    def search_albums(self, artist=None, genre=None, year=None):
        results = list(self.albums.values())
        if artist:
            results = [a for a in results if a.artist.lower() == artist.lower()]
        if genre:
            results = [a for a in results if a.genre and a.genre.lower() == genre.lower()]
        if year:
            results = [a for a in results if a.year == year]
        print(f"\n Album search results:")
        if results:
            for i, a in enumerate(results, 1):
                print(f"  {i}. {a}")
        else:
            print("No matches found.")
        return results

    def search_artists(self, name=None):
        results = list(self.artists.values())
        if name:
            results = [a for a in results if name.lower() in a.name.lower()]
        print(f"\n Artist search results:")
        if results:
            for i, a in enumerate(results, 1):
                print(f"  {i}. {a}")
        else:
            print("No matches found.")
        return results

    # Sort Songs 
    def sort_songs(self, by="title", reverse=False):
        """
        """
        valid_keys = {"title", "artist", "album", "duration", "play_count"}
        if by not in valid_keys:
            raise ValueError(f"Invalid sort key '{by}'. Choose from: {', '.join(valid_keys)}")


        songs_list = list(self.songs.values())

        def song_album_key(song):
            for album in self.albums.values():
                if song in album.songs:
                    return album.title.lower()
            return ""

    
        if by == "album":
            key_func = song_album_key
        elif by == "duration":
    
            key_func = lambda s: s.duration.total_seconds()
        else:
            if by in ("title", "artist"):
                key_func = lambda s: attrgetter(by)(s).lower()
            else:
                key_func = attrgetter(by)

        sorted_list = sorted(songs_list, key=key_func, reverse=reverse)


        print(f"\n Songs sorted by {by}{' (descending)' if reverse else ''}:")
        for idx, s in enumerate(sorted_list, 1):
            print(f"  {idx}. {s}")

        return sorted_list


    # Statistics 
    def most_played_songs(self, top_n=5):
        sorted_songs = sorted(self.songs.values(), key=lambda s: s.play_count, reverse=True)
        print(f"\n Top {top_n} most played songs:")
        for i, s in enumerate(sorted_songs[:top_n], 1):
            print(f"  {i}. {s} [{s.play_count} plays]")
        return sorted_songs[:top_n]

    def longest_songs(self, top_n=5):
        sorted_songs = sorted(self.songs.values(), key=lambda s: s.duration.total_seconds(), reverse=True)
        print(f"\n Top {top_n} longest songs:")
        for i, s in enumerate(sorted_songs[:top_n], 1):
            minutes, seconds = divmod(s.duration.seconds, 60)
            print(f"  {i}. {s.title} by {s.artist} ({minutes}:{seconds:02d})")
        return sorted_songs[:top_n]

    def songs_per_artist(self):
        print("\n Songs per artist:")
        for artist in self.artists:
            count = sum(1 for s in self.songs.values() if s.artist == artist)
            print(f"  {artist}: {count} song(s)")

    def albums_per_artist(self):
        print("\n Albums per artist:")
        for artist, obj in self.artists.items():
            print(f"  {artist}: {len(obj.albums)} album(s)")

    def total_library_duration(self):
        total = sum((s.duration for s in self.songs.values()), start=timedelta())
        minutes, seconds = divmod(total.seconds, 60)
        print(f"\n Total library duration: {minutes} minutes, {seconds} seconds")
        return total

    # Saving files
    def save_to_file(self, filename="music_library.json"):
        if not filename.endswith(".json"):
            raise InvalidFileFormatError(filename)
        data = {
            "songs": [
                {"title": s.title, "artist": s.artist, "duration": s.duration.seconds,
                 "year": s.year, "genre": s.genre, "play_count": s.play_count}
                for s in self.songs.values()
            ],
            "albums": [
                {"title": a.title, "artist": a.artist, "year": a.year,
                 "genre": a.genre, "songs": [s.title for s in a.songs]}
                for a in self.albums.values()
            ],
            "artists": [
                {"name": art.name, "albums": [al.title for al in art.albums]}
                for art in self.artists.values()
            ],
            "playlists": [
                {"name": p.name, "songs": [s.title for s in p.songs]}
                for p in self.playlists.values()
            ],
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f" Library saved to {filename}")

    def load_from_file(self, filename="music_library.json"):
        if not filename.endswith(".json"):
            raise InvalidFileFormatError(filename)
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File not found: {filename}")

        with open(filename, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                raise InvalidFileFormatError(filename)

        self.__init__()  # clear current data

        # Rebuild songs
        for s in data.get("songs", []):
            song = Song(s["title"], s["artist"], s["duration"], s.get("year"), s.get("genre"))
            song.play_count = s.get("play_count", 0)
            self.songs[s["title"]] = song

        # Rebuild albums
        for a in data.get("albums", []):
            album = Album(a["title"], a["artist"], a.get("year"), a.get("genre"))
            for song_title in a["songs"]:
                if song_title in self.songs:
                    album.add_song(self.songs[song_title])
            self.add_album(album)

        # Rebuild playlists
        for p in data.get("playlists", []):
            playlist = Playlist(p["name"])
            for song_title in p["songs"]:
                if song_title in self.songs:
                    playlist.add_song(self.songs[song_title])
            self.add_playlist(playlist)

        # Rebuild artists
        for a in data.get("artists", []):
            artist_obj = Artist(a["name"])
            for album_title in a["albums"]:
                if album_title in self.albums:
                    artist_obj.add_album(self.albums[album_title])
            self.add_artist(artist_obj)

        print(f" Library loaded from {filename}")

    # Display
    def summary(self):
        print("\n===  Music Library Summary ===")
        print(f"Artists: {len(self.artists)}")
        print(f"Albums: {len(self.albums)}")
        print(f"Songs: {len(self.songs)}")
        print(f"Playlists: {len(self.playlists)}")
        print("===============================")

def most_played_songs(self, top_n=5):
    sorted_songs = sorted(self.songs.values(), key=lambda s: s.play_count, reverse=True)
    print(f"\n Top {top_n} most played songs:")
    for i, s in enumerate(sorted_songs[:top_n], 1):
        print(f"  {i}. {s} [{s.play_count} plays]")
    return sorted_songs[:top_n]


def longest_songs(self, top_n=5):
    sorted_songs = sorted(self.songs.values(), key=lambda s: s.duration.total_seconds(), reverse=True)
    print(f"\n Top {top_n} longest songs:")
    for i, s in enumerate(sorted_songs[:top_n], 1):
        minutes, seconds = divmod(s.duration.seconds, 60)
        print(f"  {i}. {s.title} by {s.artist} ({minutes}:{seconds:02d})")
    return sorted_songs[:top_n]


def songs_per_artist(self):
    print("\n Songs per artist:")
    for artist, obj in self.artists.items():
        count = sum(1 for s in self.songs.values() if s.artist == artist)
        print(f"  {artist}: {count} song(s)")


def albums_per_artist(self):
    print("\n Albums per artist:")
    for artist, obj in self.artists.items():
        print(f"  {artist}: {len(obj.albums)} album(s)")


def total_library_duration(self):
    total = sum((s.duration for s in self.songs.values()), start=timedelta())
    minutes, seconds = divmod(total.seconds, 60)
    print(f"\n Total library duration: {minutes} minutes, {seconds} seconds")
    return total
