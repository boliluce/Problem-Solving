# DFS와 BFS
from collections import deque

def BFS(graph, root):
    deq = deque([root])
    visit = []

    while deq:
        n = deq.popleft()
        if n not in visit:
            visit.append(n)
            if n in graph:
                temp = list(set(graph[n])-set(visit))
                temp.sort()
                deq.extend(temp)

    return " ".join(str(i) for i in visit)

def DFS(graph, root):
    stack = [root]
    visit = []

    while stack:
        n = stack.pop()
        if n not in visit:
            visit.append(n)
            if n in graph:
                temp = list(set(graph[n])-set(visit))
                temp.sort(reverse=True)
                stack += temp

    return " ".join(str(i) for i in visit)

node, edge, root = list(map(int, input().split(' ')))

graph = {}
for i in range(edge):
    n1, n2 = list(map(int, input().split(' ')))

    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

print(DFS(graph,root))
print(BFS(graph,root))

