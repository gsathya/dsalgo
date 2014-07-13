# http://problemotd.com/problem/odd-array/
import sys
import random

arr = range(1, 5)
odd = []
even = []

def is_odd(x):
    return (x % 2) != 0

for x in arr:
    if is_odd(x):
        odd.append(x)
    else:
        even.append(x)

if len(odd) == 0:
    print "All even elements"
    sys.exit()

ans = []

for x in even:
    x = x + odd[0] + random.choice(even)
    ans.append(x)

ans = ans + odd
print ans
