class Song:
    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

class Album:
    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist('Various artist')
        else:
            self.artist = artist

        self.tracks = []
    def add__song(self, song, position=None):
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:

    def __init__(self,name):
        self.name=name
        self.album=[]

    def add_album(self,album):
        self.album.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open('albums.txt','r') as albums:
        for lines in albums:
            #Data row should consist of (artist,album,year,song)
            artist_field,album_field,year_field,song_field = tuple(lines.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field,album_field,year_field,song_field))

            if new_artist is None:
                new_artist=Artist(artist_field)
            elif new_artist.name!=artist_field:
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist=Artist(artist_field)
                new_album=None
if __name__== "__main__":
    load_data()