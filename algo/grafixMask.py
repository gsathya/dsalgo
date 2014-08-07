from collections import deque

def neighbors(node):
    (x, y) = node
    for i in range(-1, 2):
        for j in range(-1, 2):
            yield (x+i, y+j)

def dfs(start, visited={}):
    area = 0

    q = deque()
    q.append(start)
    if start in visited:
        return 0
    visited[start] = True

    while q:
        node = q.pop()
        (x, y) = node

        if x < 0 or x > 399:
            continue

        if y < 0 or y > 599:
            continue
        
        area += 1

        for i in neighbors(node):
            if i in visited:
                continue
            else:
                visited[i] = True
                q.append(i)

    return area

visited = {}
result = []
for i in range(400):
    for j in range(292, 308):
        visited[(i, j)] = True

for i in range(400):
    for j in range(600):
        ans = dfs((i, j), visited)
        if ans != 0:
            result.append(ans)

print result
