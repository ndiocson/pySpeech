from graph import Graph
from word import Word


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
    word to its corresponding phoneme by creating a directed edge.

    For each vertex created, a simple ID is appended to the word signifying
    the path to that word's pronunciation. 

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


def get_pronounce(word, graph):
    '''
    Starts at the vertex containing the specified word. Using the word's ID,
    traverse the graph using only the edges corresponding to that ID, and
    append each resulting vertex to a list. The list should contain the word's
    phonemes in order.

    Args:
    word - word used as starting point
    graph - word graph mapping each word to phoneme set

    Returns: list of ordered phonemes corresponding to specified word
    '''

    try:
        # get phonemes of word from graph
        phonemes = graph.neighbours(word.upper())
    except ValueError:
        # if the word cannot be found from the graph, return the word
        return word

    # if the word is found in the graph, return its list of phonemes
    return phonemes


def get_similar(word, graph):
    '''
    If a word that is not already in the graph is detected, this method is
    used to find the similar words from the total word list

    Args:
    word - unknown word as string
    graph - word graph mapping each word to phoneme set

    Returns: list of similar word(s) to the one given
    '''

    words = make_list('Words.txt')
    length = len(words)
    i = int(length/2)
    curr = words[i]
    queue = word.upper().strip()

    k = 0
    lo = 0
    hi = length
    # last = words[i]
    while True:
        if ord(queue[k]) > ord(curr[k]):
            lo = i
        else:
            hi = i

        length = hi - lo
        i = length//2 + lo
        curr = words[i]

        try:
            if curr[k] == queue[k]:
                k += 1

            print(curr, k)
            if (curr[:k] == queue[:k]) and (len(curr) == len(queue)):
                break

        except IndexError:
            return curr.lower()

    # k = lo = 0
    # hi = length
    # while True:
    #
    #     if curr[k] == queue[k]:
    #         print(curr)
    #         k += 1
    #
    #     if ord(queue[k]) > ord(curr[k]):
    #         lo = i
    #     elif ord(queue[k]) < ord(curr[k]):
    #         hi = i
    #
    #     length = hi - lo
    #     i = int(length/2) + lo
    #     curr = words[i]
    #
    #     if (curr[:k] == queue[:k]) and (len(curr) == len(queue)):
    #         return curr.lower()


if __name__ == "__main__":
    phonemes = create_phoneme_graph("Symbols.txt")
    graph = create_word_graph("Words.txt", phonemes)

    while True:
        sentence = input("Enter a sentence: ")
        for i in sentence.split():
            phoneme_list = get_pronounce(i, graph)
            if type(phoneme_list) is not list:
                sim = get_similar(phoneme_list, graph)
                print("'{}' is an unknown word; similar to '{}'"
                    .format(phoneme_list, sim))
            else:
                print(phoneme_list)
