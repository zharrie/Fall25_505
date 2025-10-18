# Build Playlist class that contains songs
import pandas as pd
import numpy as np
import os


# Implement exceptions for duplicate songs
class SongDuplicate(Exception):
    def __init__(self, value):
        self.value = value


class Playlist:
    def __init__(self, playlist_name):
        self.playlist_name = playlist_name
        self.list_of_songs = []


    def add_songs(self, list_of_songs_to_add_to_playlist):
        for song in list_of_songs_to_add_to_playlist:
            try:
                # check if we already added this title into this playlist
                # new_list = []
                # for s in self.list_of_songs:
                #     new_list.append(s.title)
                # if song.title in new_list:
                if song.title in [s.title for s in self.list_of_songs]:
                    raise SongDuplicate(f'Duplicate song: {song.title}')
                else:
                    self.list_of_songs.append(song)
            except SongDuplicate as e:
                print(f"Exception occurred: {e}")


    def sort(self, key):
        valid_sort_keys = ['title', 'artist', 'album', 'duration', 'play_count']

        if key not in valid_sort_keys:
            print(f'Not a valid key to sort, should be one of {valid_sort_keys}')
        else:
            print(f"Sorting by {key}")
            print(f"Old sort: {[s.title for s in self.list_of_songs]}")
            # https://stackoverflow.com/questions/72899/how-can-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary-in-python
            if key == 'title':
                self.list_of_songs = sorted(self.list_of_songs, key=lambda x: x.title)
            elif key == 'artist':
                self.list_of_songs = sorted(self.list_of_songs, key=lambda x: x.artist)
            elif key == 'album':
                self.list_of_songs = sorted(self.list_of_songs, key=lambda x: x.album)
            elif key == 'duration':
                self.list_of_songs = sorted(self.list_of_songs, key=lambda x: x.duration)
            elif key == 'play_count':
                self.list_of_songs = sorted(self.list_of_songs, key=lambda x: x.play_count)
            print(f"New sort: {[s.title for s in self.list_of_songs]}")
            

    
    def search(self, key, value_to_search):
        valid_search_keys = ['artist', 'album', 'genre', 'year']

        if key not in valid_search_keys:
            print(f'Not a valid key to search, should be one of {valid_search_keys}')
        else:
            print(f"Searching by {key}: {value_to_search}")
            for instance in self.list_of_songs:
                if key == 'artist' and instance.artist == value_to_search:
                    print(f"Song: {instance.title}, artist: {instance.artist}")
                elif key == 'album' and instance.album == value_to_search:
                    print(f"Song: {instance.title}, album: {instance.album}")
                elif key == 'genre' and instance.genre == value_to_search:
                    print(f"Song: {instance.title}, genre: {instance.genre}")
                elif key == 'year' and instance.year == value_to_search:
                    print(f"Song: {instance.title}, year: {instance.year}")


    def print_statistics(self, key):
        valid_statistics_keys = ['most_played', 'longest_songs', 'overall_stats']

        if key not in valid_statistics_keys:
            print(f'Not a valid key to provide statistics for, should be one of {valid_statistics_keys}')
        else:
            stats_list = []
            if key == 'most_played':
                for instance in self.list_of_songs:
                    stats_list.append([instance.title, instance.play_count])
                df = pd.DataFrame(stats_list, columns = ['title', 'play_count'])
                most_played = df.nlargest(1, 'play_count')
                print("Top 1 song by play count:")
                print(f"{most_played}")
            elif key == 'longest_songs':
                for instance in self.list_of_songs:
                    stats_list.append([instance.title, instance.duration])
                df = pd.DataFrame(stats_list, columns = ['title', 'duration'])
                longest_song = df.nlargest(3, 'duration')
                print("Top 3 songs by duration:")
                print(f"{longest_song}")
            elif key == 'overall_stats':
                n = np.array([i.duration for i in self.list_of_songs])
                print(f"Duration mean: {n.mean():.2f}, max: {n.max()}, min: {n.min()}")
                
            

    def save_to_json(self):

        #Saving json to the current directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)


        saving_list = []

        for instance in self.list_of_songs:
            saving_list.append([instance.title, instance.album, instance.artist, instance.genre, instance.duration, instance.year, instance.play_count])
        df = pd.DataFrame(saving_list, columns = ['title', 'album', 'artist', 'genre', 'duration', 'year', 'play count'])

        df.to_json('output.json', orient = "records")
