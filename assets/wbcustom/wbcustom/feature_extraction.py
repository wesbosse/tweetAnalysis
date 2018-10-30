import numpy as np
import pandas as pd
from sklearn.base import TransformerMixin, BaseEstimator
from nltk.sentiment.vader import SentimentIntensityAnalyzer;

class FeatureExtraction(BaseEstimator, TransformerMixin):
    '''
    Accepts a df, returns feature list based on params given
    converts a corpus into a feature dataframe containing text and several numeric features
    '''

    def __init__(self):
        '''

        '''
        # curse = []
        # racial = []
        # sexual = []
        # substance_use = []
        self.fn = ['suspect']
        self.nsfw = ['anal', 'anus', 'arse', 'ass', 'ballsack', 'balls', 'bastard', 'bitch', 'biatch', 'bloody',
                     'blowjob', 'blow job', 'bollock', 'bollok', 'boner', 'boob', 'bugger', 'bum', 'butt', 'buttplug',
                     'clitoris', 'cock', 'coon', 'crap', 'cunt', 'damn', 'dick', 'dildo', 'dyke', 'fag', 'feck',
                     'fellate', 'fellatio', 'felching', 'fuck', 'f u c k', 'fudgepacker', 'fudge packer', 'flange',
                     'Goddamn', 'God damn', 'hell', 'homo', 'jerk', 'jizz', 'knobend', 'knob end', 'labia', 'lmao',
                     'lmfao', 'muff', 'nigger', 'nigga', 'omg', 'penis', 'piss', 'poop', 'prick', 'pube', 'pussy',
                     'queer', 'scrotum', 'sex', 'shit', 's hit', 'sh1t', 'slut', 'smegma', 'spunk', 'tit', 'tosser',
                     'turd', 'twat', 'vagina', 'wank', 'whore']


    def contains_suspect_word(self, document, word_list=None):
        '''
        checks document against provided word list to check for presence of suspect words
        '''
        if word_list is None:
            word_list = self.nsfw
        suspect = set(word_list).intersection(document.split(' '))
        return 1 if suspect else 0

    def get_feature_names(self):
        return self.fn

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        '''
        convert our corpus to a feature df
        '''

        return [self.contains_suspect_word(x.lower()) for x in X]

