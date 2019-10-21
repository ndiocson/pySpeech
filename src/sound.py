import pygame

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
        self.path = '../wav/' + filename

    def play(self):
        # pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.mixer.pre_init(39250, -16, 2, 64)
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load(self.path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

    def __str__(self):
        return ('{}' .format(self.path))
