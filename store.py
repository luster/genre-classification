#!ENV/bin/python

from CONFIG import DATABASE_HOST, DATABASE_PORT, DATABASE_NAME
from pymongo import Connection
from itunes import *

connection = Connection(DATABASE_HOST, DATABASE_PORT)
db = connection[DATABASE_NAME]

# define collection tables
itunes = db.itunes
echonest = db.echonest
lastfm = db.lastfm


