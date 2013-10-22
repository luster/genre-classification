#!/ENV/bin/python

# make queries for songs from the database here

# import the database instance
from store import *

def get_tracks_by_genre(genre, db_table):
    """Returns a list of tracks from a specific genre from the specified mongo table"""

    return db_table.find({"genre": genre.lower()})

def get_tracks_by_artist(artist, db_table):
    """Returns a list of tracks from a specific artist from the specified mongo table"""

    return db_table.find({"artist": artist.lower()})
