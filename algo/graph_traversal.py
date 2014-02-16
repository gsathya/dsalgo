graph = {
    'a' : ['b', 'c'],
    'b' : ['d', 'a'],
    'c' : ['a', 'd'],
    'd' : ['a'],
    'e' : []
}

from Queue import Queue

def bfs(start, graph, vertices):
    if start == None:
        return -1

    q = Queue()

    visited = {}
    for vertex in vertices:
        visited[vertex] = False

    q.put(start)
    visited[start] = True
    
    while not q.empty():
        node = q.get()
        print node

        for n in graph[node]:
            if not visited[n]:
                q.put(n)
                visited[n] = True

def dfs(start, graph, vertices):
    if start == None:
        return -1

    stack = []
    visited = {}

    for vertex in vertices:
        visited[vertex] = False

    stack.append(start)

    while len(stack) > 0:
        node = stack.pop()
        visited[node] = True

        print node

        for n in graph[node]:
            if not visited[n]:
                stack.append(n)

def dfs_recursive(start, graph, vertices):
    if start == None:
        return -1

    visited = {}

    for vertex in vertices:
        visited[vertex] = False

    visited[start] = True
    dfs_recursive_util(start, graph, visited)


def dfs_recursive_util(start, graph, visited):
    if start == None:
        return
    
    print start

    for n in graph[start]:
        if not visited[n]:
            visited[n] = True
            dfs_recursive_util(n, graph, visited)

print "BFS:"
bfs('a', graph, ['a', 'b', 'c', 'd', 'e'])
print "\nDFS:"
dfs('a', graph, ['a', 'b', 'c', 'd', 'e'])
print "\nDFS recursively:"
dfs_recursive('a', graph, ['a', 'b', 'c', 'd', 'e'])

