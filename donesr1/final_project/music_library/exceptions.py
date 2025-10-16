class MusicLibraryError(Exception):
    pass


class DuplicateSongError(MusicLibraryError):
    def __init__(self, title):
        super().__init__(f"Song '{title}' already exists in the library.")


class InvalidFileFormatError(MusicLibraryError):
    def __init__(self, filename):
        super().__init__(f"Invalid file format: '{filename}'. Expected a .json file.")
