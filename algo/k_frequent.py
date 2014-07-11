# usage - $python k_frequent.py log_file k
import sys
import heapq

freq = {}
# running time is O(n)
with open(sys.argv[1]) as fh:
    for line in fh.readlines():
        freq[line] = freq.get(line.strip(), 0) + 1

q = []
i = 0
k = int(sys.argv[2])

# running time is O(nlogk)
for key, value in freq.items():
    # push first k vars into q
    if i < k:
        heapq.heappush(q, (value, key))
    else:
        # push value only if it's bigger than smallest val in q
        top = q[0]
        if value > top[0]:
            heapq.heapreplace(q, (value, key))
    i += 1

while len(q) > 0:
    value, key = heapq.heappop(q)
    print key

