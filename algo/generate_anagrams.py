import sys
from random import shuffle 

word = list(sys.argv[1])
anagrams = []

for i in range(10):
    shuffle(word)
    anagrams.append(''.join(word))

print anagrams
