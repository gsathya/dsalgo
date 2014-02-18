graph = {
    'a' : ['b', 'c'],
    'b' : ['c'],
    'c' : []
}

def top_sort_util(graph, visited, stack, v):
    visited[v] = True
    
    for i in graph[v]:
        if visited[i] == False:
            top_sort_util(graph, visited, stack, i)
    
    stack.append(v)
    
def top_sort(graph):
    visited = {}
    stack = []
    
    for v in graph.keys():
        visited[v] = False
        
    for v in graph.keys():
        if visited[v] == False:
            top_sort_util(graph, visited, stack, v)
            
    for i in stack:
        print i

top_sort(graph)
