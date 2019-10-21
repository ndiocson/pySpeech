from graph import Graph
import num

def make_list(filename):
    '''
    Goes through text file and appends each phoneme or word to a list

    Args:
    filename - name of .txt file that contains phonemes or words

    Returns: List containing words or phonemes as individual elements in order
    '''

    # open and read from specified file
    open_file = open(filename, 'r')
    some_list = []

    # loop through the file and append the word or phoneme to a list
    for i in open_file:
        if "(" not in i.split()[0]:
            some_list.append(i.split()[0])

    return some_list

def create_phoneme_graph(filename):
    '''
    Goes through file and creates a vertex for each phoneme

    Args:
    filename - name of .txt file that contains phonemes

    Returns: Graph containing phonemes as vertices
    '''

    # open and read from specified file
    phoneme_file = open(filename, 'r')
    phonemes = Graph()

    # loop through the file and create a vertex for each phoneme
    for p in phoneme_file:
        phonemes.add_vertex(p.split()[0])

    return phonemes

def create_word_graph(filename, graph):
    '''
    Goes through file and creates vertex for each word, then maps each
    word to its corresponding phoneme(s) by creating directed edge(s).

    Args:
    filename - name of .txt file that contains words
    graph - graph that contains phonemes as vertices

    Returns: Directed graph containing words and phonemes
    '''

    # open and read from specified file
    word_file = open(filename, 'r')

    # loop through the file to create a vertex for each word and make
    # directed edges between a word and its phonemes
    for w in word_file:
        # add word to graph
        if "(" not in w.split()[0]:

            # append word as seperate vertex in graph
            graph.add_vertex(w.split()[0])

            # get the list of phonemes of the current word
            p_list = [str(p) for p in w.split()[1::]]

            # add directed edge between word and each of its phonemes
            for i in range(len(p_list)):
                graph.add_edge((w.split()[0], p_list[i]))

    return graph

def remove_punct(word):
    '''
    Takes a word and removes the punctuation from it such that only letters
    remain

    Args:
    word - a string that may or may not conatin punctuation

    Returns: new word without that punctuation of the original
    '''

    punct = '''!()-[]"{""}";:'"|\,<>./?@#$%^&*_~'''

    new_word = ""
    for w in word:
        if w not in punct:
            new_word += w

    return new_word

def get_pronounce(word, graph):
    '''
    Finds the phonemes of a given word by returning the word's neighbours.

    Args:
    word - word used as starting point
    graph - word graph mapping each word to phoneme set

    Returns: list of ordered phonemes corresponding to specified word
    '''

    phonemes = list()
    new_word = remove_punct(word)

    try:
        # get and return phonemes of word from graph
        return graph.neighbours(new_word.upper())

    except ValueError:

        try:
            # if the 'word' is a number in the numbers dictionary, return the key
            if word in num.numbers:
                return graph.neighbours(num.numbers[new_word].upper())

            # if not, get the corresponding word representation for the 'word'
            # as a list, then subsequently get the phonemes of each item
            if len(new_word) <= 4:
                num_queue = num.parse_num(new_word)
            else:
                num_queue = num.literal_num(new_word)

            for n in num_queue:
                phonemes += graph.neighbours(n.upper())

            return phonemes

        except KeyError:
            # else, if the word is neither a number nor in the word graph,
            # return None
            return None

def get_similar(word, graph):
    '''
    If a word that is not already in the graph is detected, this method is
    used to find the similar words from the total word list using a
    divide and conquer style algorithm

    Args:
    word - unknown word as string
    graph - word graph mapping each word to phoneme set

    Returns: list of similar word(s) to the one given
    '''

    # get the list of words and length, set i to the midpoint of the list
    # use i to get the current word and store the called word as queue
    words = make_list('text/Words.txt')
    length = len(words)
    i = int(length / 2)
    curr = words[i]
    queue = word.upper().strip()

    # initalize variables for the  following algorithm
    k = 0  # index for letters
    lo = 0   # lower bound
    hi = length  # higher bound
    prev_lo = 0  # previous lower bound
    prev_hi = 0  # previous higher bound
    prev_word = ""
    poss = ""

    while True:
        try:
            # set the bounds using the first letter of queue
            if k == 0:

                # the upper bound ends just before the next letter
                hi = words.index(chr(ord(queue[k]) + 1)) - 1

                # the lower bound starts at queues first letter
                lo = words.index(chr(ord(queue[k])))

            # if the previous letter of current is below queues' previous char.
            elif ord(queue[k - 1]) > ord(curr[k - 1]):

                # increase the lower bound to i
                lo = i

            # if the previous letter of current is above queues' previous char.
            elif ord(queue[k - 1]) < ord(curr[k - 1]):

                # decrease upper bound to i
                hi = i

            # if the current letter of current is above queues' current char.
            elif ord(queue[k]) > ord(curr[k]):

                # increase the lower bound to i
                lo = i

            # otherwise decrease the upper bound to i
            else:
                hi = i

        # return current word if an index error occurs in the try block
        except IndexError:
            return curr.lower()

        # find the new length with the new bounds and the new middle word
        length = hi - lo
        i = int(length / 2) + lo
        prev_word = curr
        curr = words[i]

        # while the current word is smaller than the index...
        while len(curr) < k + 1:
            # go to the previous word in the list to prevent an index error
            curr = words[i - 1]

        try:
            # for the first letter being analyzed...
            if k == 0:

                # if the first letter of current is the same as queue's
                if curr[k] == queue[k]:

                    # increase the index and save the previous bounds
                    k += 1
                    prev_lo = lo
                    prev_hi = hi

            # if the current word matches queue up to the current index...
            elif curr[:k + 1] == queue[:k + 1]:

                # increase the index and save the previous bounds
                k += 1
                prev_lo = lo
                prev_hi = hi

            # a run on loop is indicated if previous is equal to the current
            elif prev_word == curr:

                # for each word in between the previous bounds
                for i in range(prev_lo, prev_hi):

                    # return the word if it shares common charcaters and length
                    if words[i][:k] == queue[:k] and len(words[i]) == len(queue):
                        return words[i].lower()

                    # if the word only shares common charcaters and not length
                    elif words[i][:k] == queue[:k]:
                        # save the word as a possible output
                        poss = words[i]

                # if no word satisfied the first if statement in the for loop
                # return the last possible word saved
                return poss.lower()

            # return current if it shares the same characters and length as
            # queue
            if (curr[:k + 1] == queue[:k + 1]) and (len(curr) == len(queue)):
                return curr.lower()

        # return the current word if an index error occurs in the try block
        except IndexError:
            return curr.lower()
