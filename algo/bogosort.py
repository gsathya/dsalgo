#  http://problemotd.com/problem/bogosort/

from random import shuffle

arr = range(5)
shuffle(arr)

def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

while not is_sorted(arr):
    shuffle(arr)

print arr
