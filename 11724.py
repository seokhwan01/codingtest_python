#연결 요소의 개수

import sys
sys.setrecursionlimit(10**6)
# from collections import defaultdict
n,m=map(int,sys.stdin.readline().split())
# graph=defaultdict(list)#없는 키 접근 하면 자동으로 빈 리스트 만들어줌
graph={}
for i in range(1,n+1):
    graph[i]=[]

for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited=[False]*(n+1)


def dfs(start):
    visited[start]=True

    for element in graph[start]:
        if not visited[element]:
            dfs(element)

count=0
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        count+=1

print(count)
# input("종료방지")