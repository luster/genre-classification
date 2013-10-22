#!ENV/bin/python

from pyItunes import *
from pprint import pprint

filename = 'data/library.xml'

def lib_parse(filename):
    """Takes an iTunes library xml file and converts it to a list of song dicts."""
    l = Library(filename)
    songs = []

    for id,song in l.songs.items():
        songs.append(
                {
                    "name": song.name,
                    "artist": song.artist,
                    "album_artist": song.album_artist,
                    "composer": song.composer,
                    "album": song.album,
                    "genre": song.genre,
                    "kind": song.kind,
                    "size": song.size,
                    "total_time": song.total_time,
                    "track_number": song.track_number,
                    "year": song.year,
                    "date_modified": song.date_modified,
                    "date_added": song.date_added,
                    "bit_rate": song.bit_rate,
                    "sample_rate": song.sample_rate,
                    "comments": song.comments,
                    "rating": song.rating,
                    "album_rating": song.album_rating,
                    "play_count": song.play_count,
                    "location": song.location,
                    "compilation": song.compilation,
                    "grouping": song.grouping,
                    "lastplayed": song.lastplayed,
                    "length": song.length
                    }
                )
    return songs

if __name__ == '__main__':
    songs = lib_parse(filename)
