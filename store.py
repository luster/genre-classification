#!ENV/bin/python

from CONFIG import DATABASE_HOST, DATABASE_PORT, DATABASE_NAME
from pymongo import MongoClient

# start a mongo client and connect to database
client = MongoClient(DATABASE_HOST, DATABASE_PORT)
db = client[DATABASE_NAME]

# define collection tables
table = 'echonest'
echonest = db[table]

def main():
    pass

if __name__ == '__main__':
    # import data source & store
    main()
