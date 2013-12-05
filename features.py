import MFCC
import numpy as np
from scipy.io import wavfile
from store import Store

def compute_mfcc(track, db):
    """ Computes the MFCC of a track and stores it in database"""
    sampleRate, signal = wavfile.read(track['filepath'])
    signal = np.mean(signal, 1) # average stereo audio signals together
    mfcc = MFCC.extract(signal, sampleRate, show=False)
    mfcc = mfcc[:15]
    mfcc_mean = np.mean(mfcc, 0).tolist()
    mfcc_var = np.cov(mfcc).flatten().tolist()
    mfcc_feature = mfcc_mean + mfcc_var
    db.store_mfcc(track['_id'], mfcc_feature)
    return mfcc_feature
