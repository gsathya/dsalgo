import sys
import shuffle from random

word = list(sys.argv[1])
anagrams = []

for i in range(10):
    anagrams.append(''.join(shuffle(word)))

print anagrams
