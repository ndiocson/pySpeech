numbers = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
           '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine',
           '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen',
           '14': 'fourteen', '15': 'fifteen', '16': 'sixteen',
           '17': 'seventeen', '18': 'eighteen', '19': 'nineteen',
           '20': 'twenty', '30': 'thirty', '40': 'forty', '50': 'fifty',
           '60': 'sixty', '70': 'seventy', '80': 'eighty', '90': 'ninety'}

def parse_num(num):
    '''
    This function will take a number up to 9999 and convert it to it's 'word'
    representation.
    For example, if the number 3452 is passed, this function should return:
    ['three', 'thousand', 'four', 'hundred', 'fifty', 'two']

    Args:
    num - an string of an integer

    Returns: a 'word' representation of the number as a list
    '''

    # initialize converted word list
    word = []

    # for each digit in the number, determine its placement with respect
    # to the overall number and append zeros where necessary
    for i in range(len(num)):
        s = num[i]

        for j in range(len(num) - (i + 1)):
            s += '0'

        # if the first digit of the current number is not a zero, append the
        # corresponding word representation to the converted word list
        if s[0] != '0':
            # if s is already in the numbers dictionary, append its item
            if s in numbers:
                word.append(numbers[s])
                continue

            # else, first append the first digit of s, then its prefix
            word.append(numbers[num[i]])
            if "00" in s and len(s) is 3:
                word.append("hundred")
            elif "000" in s and len(s) is 4:
                word.append("thousand")

    return word

def literal_num(num):
    '''
    If the number is larger than 9999, return a list of the 'word'
    representation of each digit from the numbers dictionary.
    For example, if the number 19234 is passed, this functin will return:
    ['one, 'nine', 'two', 'three', 'four']

    Args:
    num - a string of an integer

    Returns: a list containing the 'word' representation of each digit in the
    original number
    '''
    word = []
    for i in range(len(num)):
        word.append(numbers[num[i]])

    return word
