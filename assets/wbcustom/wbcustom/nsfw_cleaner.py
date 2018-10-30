import pandas as pd
from sklearn.base import TransformerMixin, BaseEstimator


class NsfwCleaner(BaseEstimator, TransformerMixin):
    '''
    Accepts a df, returns feature list based on params given
    converts a corpus into a feature dataframe containing text and several numeric features
    '''

    def __init__(self):
        '''

        '''

        self.nsfw = ['anal', 'anus', 'arse', 'ass', 'ballsack', 'balls', 'bastard', 'bitch', 'biatch', 'bloody',
                     'blowjob', 'blow job', 'bollock', 'bollok', 'boner', 'boob', 'bugger', 'bum', 'butt', 'buttplug',
                     'clitoris', 'cock', 'coon', 'crap', 'cunt', 'damn', 'dick', 'dildo', 'dyke', 'fag', 'feck',
                     'fellate', 'fellatio', 'felching', 'fuck', 'f u c k', 'fudgepacker', 'fudge packer', 'flange',
                     'Goddamn', 'God damn', 'hell', 'homo', 'jerk', 'jizz', 'knobend', 'knob end', 'labia', 'lmao',
                     'lmfao', 'muff', 'nigger', 'nigga', 'omg', 'penis', 'piss', 'poop', 'prick', 'pube', 'pussy',
                     'queer', 'scrotum', 'sex', 'shit', 's hit', 'sh1t', 'slut', 'smegma', 'spunk', 'tit', 'tosser',
                     'turd', 'twat', 'vagina', 'wank', 'whore']


    def remove_suspect_words(self, df, word_list):
        '''
        removes suspect words to test performance once they are removed.
        this is an attempt to consolidate features to allow our model to dig in more, we will see how it goes.
        '''
        for column in df.columns:
            if column not in word_list:
                df = df.drop(columns=[column])

        return df

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        '''
        convert our corpus to a feature df
        '''
        return self.remove_suspect_words(X, self.nsfw)
