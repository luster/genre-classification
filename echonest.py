#!ENV/bin/python
'''
Quick Script Which Retrieves Data From Echonest for Use in the Machine Learning Algorithm
'''

from pyechonest import config, playlist
from CONFIG import echonest, algorithm
from pydub import AudioSegment
import hashlib
import urllib
import logging
import os
import time

config.ECHO_NEST_API_KEY = echonest['apiKey']
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

api_calls = 0
songs_added = 0

# Retrieves song preview, stores it in directory structure
def download_song(genre, song):
    logger.debug('Downloading Song: %s' % song)
    global api_calls
    global songs_added
    try:
        api_calls += 1
        if api_calls >= 20:
            time.sleep(20) # Sleep for 20 seconds to prevent going over API limit
            api_calls = 0
        tracks = song.get_tracks('7digital-US')
        preview_url = tracks[0].get('preview_url')
        logger.debug('Preview URL for Song %s: %s' % (song, preview_url))

        # Save under .wav since mp3 will be converted later
        filename = song.artist_name + '-' + song.title + '.wav'
        filename = filename.replace(' ', '_')
        # Hash filename for directory structure
        md5 = hashlib.md5()
        md5.update(filename)
        hashed_filename = md5.hexdigest()

        # Genreate folder structure if does not exist
        cur_dir = os.getcwd() + '/raw_audio'
        if not os.path.exists(cur_dir):
            os.makedirs(cur_dir)
        cur_dir += '/' + genre
        if not os.path.exists(cur_dir):
            os.makedirs(cur_dir)
        for i in range(1):
            cur_dir += '/' + hashed_filename[i]
            if not os.path.exists(cur_dir):
                os.makedirs(cur_dir)

        # Download file
        file_path = cur_dir + '/' + filename
        urllib.urlretrieve(preview_url, file_path)

        # Convert from mp3 to wav file
        song = AudioSegment.from_mp3(file_path)
        song.export(file_path, format="wav")
        songs_added += 1
        return file_path
    except Exception, e:
        print "Could not Download File", e


# Stores information about song in Mongo
def store_song(genre, song):
    file_path = download_song(genre, song)

def main():
    global songs_added
    for genre in algorithm['genres']:
        # Generate Playlist For Genre for training size as well as testing
        logger.debug('Getting Playlist for Genre: %s' % genre)
        songs_added = 0
        genre_playlist = playlist.basic(type='genre-radio', genres=[genre], \
                results=int(algorithm['training_size']*1.5), buckets=['id:7digital-US', 'tracks'])
        for song in genre_playlist:
            if songs_added < algorithm['training_size']:
                store_song(genre, song)
            else:
                break

if __name__ == '__main__':
    main()
