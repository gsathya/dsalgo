# usage - $python generate_anagrams.py foo bar
import sys
from random import shuffle

for word in sys.argv[1:]:
    word = list(word)
    anagrams = []

    for i in range(10):
        shuffle(word)
        anagrams.append(''.join(word))

    print ' '.join(anagrams)
