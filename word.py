
class Word:

    def __init__(self, word, phonemes = list()):
        '''
        Constructs an instance of class word that holds the word itself as a
        string, its ID as an integer, and a list of its phonemes
        '''

        self.word = str(word)
        self.phonemes = phonemes

    def get_word(self):
        '''
        Return word as string
        '''
        return self.word

    def get_phonemes(self):
        '''
        Return list of phonemes
        '''
        return self.phonemes
