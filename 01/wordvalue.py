from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as dict_file:
        return [line.strip() for line in dict_file.readlines()]


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word_value = 0
    for char in word:
        word_value += LETTER_SCORES.get(char.upper(), 0)
    return word_value


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    words = words or load_words()
    max_value = -1
    max_word = None
    for word in words:
        current_value = calc_word_value(word)
        if current_value > max_value:
            max_value = current_value
            max_word = word
    return max_word


if __name__ == "__main__":
    pass  # run unittests to validate
