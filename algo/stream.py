"""
In a stream of integers from 1 to n, only one number will be repeated. How can you tell what that number is?
Usage - $python stream.py n
"""
import sys
import random

n = int(sys.argv[1])
r = range(1, n+1)
r.append(random.randint(1, n))

sum1 = sum(range(1, n+1))
sum2 = sum(r)

print r
print "Duplicate number = %d" % (sum2-sum1)
