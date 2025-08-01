#DFS와 BFS
import sys
from collections import deque

def dfs(start,graph):#스택 방식
    dfs_visited=[False]*(n+1)

    stack=[start]
    while stack:
        node=stack.pop()

        if not dfs_visited[node]:
            dfs_visited[node]=True
            print(node, end=" ")

            for neighor in sorted(graph[node],reverse=True):
                if not dfs_visited[neighor]:
                    stack.append(neighor)
    print()

def bfs(start,graph):
    queue=deque([start])
    bfs_visited=[False]*(n+1)
    bfs_visited[start]=True

    while queue:
        node=queue.popleft()
        print(node,end=" ")

        for neighor in sorted(graph[node]):
            if not bfs_visited[neighor]:
                bfs_visited[neighor]=True
                queue.append(neighor)
    print()


n,m,v=map(int,sys.stdin.readline().split())
graph={}
for i in range(1,n+1):
    graph[i]=[]

for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(v,graph)
bfs(v,graph)
# print(graph)