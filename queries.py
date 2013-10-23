#!/ENV/bin/python

# make queries for song metadata from the database here
# make queries for corresponding audio files from the directory structure here
#   need hash function and directory structure


# import the database instance
from store import *

def get_tracks_by_genre(genre, db_table):
    """Returns a list of tracks from a specific genre from the specified mongo table"""

    return db_table.find({"genre": genre.lower()})

def get_tracks_by_artist(artist, db_table):
    """Returns a list of tracks from a specific artist from the specified mongo table"""

    return db_table.find({"artist": artist.lower()})

def get_raw_audio(song):
    """Get raw audio in mp3 or wav format from song input"""

    return 0
