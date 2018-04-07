
class Sound:

    def __init__(self, name):
        '''
        Constructs instance of class Sound that holds the filename
        '''
        name = name.strip()
        letters = ""
        for l in name:
            if (ord(l) >= 65 and ord(l) <= 90) or (ord(l) >= 97 and ord(l) <= 122):
                letters += l.upper()

        filename = str(letters) + ".wav"
        self.audio = filename

    def __str__(self):
        return ('{}' .format(self.audio))
