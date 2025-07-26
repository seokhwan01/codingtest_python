#바이러스
import sys
from collections import deque
n=int(sys.stdin.readline().strip())
graph={}
for i in range(1,n+1):
    graph[i]=[]

pair_num=int(sys.stdin.readline().strip())
for i in range(pair_num):
        a,b=map(int,sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

visited = [False] * (len(graph) + 1)


def bfs(start):
    count=0
    queue=deque([start])
    visited[start]=True

    while queue:
        v=queue.popleft()
        # print(f"v = {v}")

        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor]=True
                queue.append(neighbor)
                count+=1
    return count
print(bfs(1))


    
         
      