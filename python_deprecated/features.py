import MFCC
import numpy as np
from scipy.io import wavfile
from store import Store

def compute_mfcc(track, db):
    """ Computes the MFCC of a track and stores it in database"""
    sampleRate, signal = wavfile.read(track['filepath'])
    signal = np.mean(signal, 1) # average stereo audio signals together
    mfcc = MFCC.extract(signal, sampleRate, show=False)
    #mfcc = np.mean(mfcc, 0)
    mfcc_feature = mfcc.tolist()
    print 'here'
    db.store_mfcc(track['_id'], mfcc_feature)
    return mfcc_feature

def featurize(mfcc):
    mfcc = np.array(mfcc)
    mfcc_mean = np.mean(mfcc, 0)
    #mfcc = mfcc[:15]
    #mfcc_stddev = np.std(mfcc)
    #mfcc_ratio = abs(mfcc[1:] / mfcc[0:-1])
    mfcc_cov = np.cov(mfcc).flatten()
    #import pdb
    #pdb.set_trace()
    #mfcc_mean_cov = np.mean(mfcc_cov, 1)
    #mfcc_feature = mfcc_mean.tolist() + mfcc_ratio.tolist()
    #mfcc_feature.append(mfcc_stddev)
    #features = mfcc.tolist() + mfcc_ratio.tolist() + [mfcc_stddev]
    features = mfcc_mean.tolist() + mfcc_cov.tolist()
    return features
