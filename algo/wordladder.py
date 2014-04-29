import sys
from collections import deque

def bfs(g, start, end):
    q = deque([start])
    path = {}
    visited = {}

    while q:
        node = q.popleft()

        if node == end:
            return path

        for neighbour in g[node]:
            if not visited.get(neighbour, False):
                path[neighbour] = node
                visited[neighbour] = True
                q.append(neighbour)
    return None

def main(start, end):
    # temp dict
    d = {}
    # graph
    g = {}

    word_len = len(start)
    with open("wordsEn.txt") as fh:
        for line in fh.readlines():
            line = line.strip()

            # load only words we can use
            if word_len != len(line):
                continue

            # create buckets
            for i in range(len(line)):
                key = line[:i] + '_' + line[i+1:]
                if key in d:
                    d[key].append(line)
                else:
                    d[key] = [line]

    # create graph
    for key, val in d.items():
        for i in val:
            for j in val:
                if i != j:
                    if i in g:
                        g[i].append(j)
                    else:
                        g[i] = [j]

    paths = bfs(g, start, end)
    if not paths:
        print "no path found!"
        sys.exit()

    # backtrack to get path
    path = [end]
    while path[-1]!=start:
        path.append(paths[path[-1]])
    path.reverse()

    print ' -> '.join(path)

if __name__ == "__main__":
    start = sys.argv[1]
    end = sys.argv[2]
    main(start, end)
