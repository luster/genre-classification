#!ENV/bin/python

from CONFIG import DATABASE_HOST, DATABASE_PORT, DATABASE_NAME
from pymongo import MongoClient

class Store(object):
    """This opens a connection to a mongo database and allows the user to store and get track metadata."""

    # start a mongo client and connect to database
    client = MongoClient(DATABASE_HOST, DATABASE_PORT)
    db = client[DATABASE_NAME]

    def __init__(self, table='songs'):
        # define collection tables
        self.table = Store.db[table]

    def get_all_tracks(self):
        return self.table.find()

    def get_tracks_by_genre(self, genre):
        """Returns a list of tracks from a specific genre from the specified mongo table"""
        return self.table.find({"genre": genre.lower()})

    def get_tracks_by_artist(self, artist):
        """Returns a list of tracks from a specific artist from the specified mongo table"""
        return self.table.find({"artist": artist.lower()})

    def get_track(self, title, artist):
        """Get track based on title and artist from specified mongo table"""
        return self.table.find_one({"title": title, "artist": artist})

    def store_track(self, title, artist, genre, filepath, echo_id, data):
        """Store track in database with specified title, artist, and extra data."""

        post = {
                'title': title,
                'artist': artist,
                'genre': genre,
                'filepath': filepath,
                'echo_id': echo_id,
                'data': data
                }
        self.table.insert(post)

    def store_mfcc(self, track_id, mfcc):
        """Store track in database with specified title, artist, and extra data."""
        self.table.update({'_id': track_id}, {'$set': {'mfcc_tot': mfcc}})

