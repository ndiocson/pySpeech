from graph import Graph
from phoneme import Sound
import pygame
import time

def map_audio(graph):
    '''
    Goes through phoneme graph and maps each phoneme to an audio file with
    the same name

    Args:
    graph - graph containing only phonemes as vertices

    Returns: Graph mapping each phoneme to corresponding audio file
    '''

    pass


def play_audio(phoneme):
    '''
    Plays the audio file for the passed phoneme

    Args:
    phoneme - simple string
    '''

    # filename = phoneme.upper() + ".wav"
    pygame.mixer.init()
    pygame.mixer.music.load(phoneme)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

    pass


def convert(phonemes):
    '''
    Given a set/list of phonemes, play the audio of each element with a slight
    delay in between each output.

    Args:
    phonemes - set/list of phonemes
    '''

    files = []
    for p in phonemes:
        files.append(Sound(p).__str__())

    return files


if __name__ == "__main__":
    l = convert(['TH1', 'ZH0', 'V', 'SH1', 'UW0'])
    print("Original: ", *['TH1', 'ZH0', 'V', 'SH1', 'UW0'])
    print('Converted: ', *l)

    print('Playing audio...')
    for f in l:
        play_audio(str(f))
