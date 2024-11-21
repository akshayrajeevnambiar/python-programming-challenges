# Python Code Challenge #3: Sort a String
# ----------------------------------------
# Your goal is to implement a function, sort_words(), that takes a string containing one or more words separated by spaces as the input argument and returns a string containing those words sorted alphabetically.

import re

def sort_words(phrase):
    words = re.findall(r'[a-zA-Z]+', phrase)

    return ' '.join(sorted(words, key= lambda s: s.casefold()))

print(sort_words("banana ORANGE apple"))