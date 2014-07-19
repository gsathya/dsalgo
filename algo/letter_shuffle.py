# http://problemotd.com/problem/letter-shuffle/
import sys
import random

word = sys.argv[1]
f = word[0]
l = word[-1]
word = list(word[1:-1])

random.shuffle(word)

print ''.join([f]+word+[l])
