import math
from collections import deque, defaultdict

n = int(raw_input())
m = int(raw_input())
connections = m

sum = 0
graph = defaultdict(list)
visited = {}

while m > 0:
    line = raw_input().split()

    p, q = int(line[0]), int(line[1])

    graph[p].append(q)
    graph[q].append(p)

    m -= 1

def bfs(g, start):
    visited[start] = True
    q = deque([start])
    group_len = 0

    while q:
        node = q.popleft()

        group_len += 1

        for neighbour in g[node]:
            if not visited.get(neighbour, False):
                visited[neighbour] = True
                q.append(neighbour)

    return group_len

total_cost = 0
for key in graph.keys():
    if key not in visited:
        group_len = bfs(graph, key)
        total_cost += math.ceil(math.sqrt(group_len))
        n -= group_len

total_cost += n
print int(total_cost)
