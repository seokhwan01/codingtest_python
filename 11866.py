#백준 11866번: 요세푸스 문제0
import sys
from collections import deque
n,k=map(int,sys.stdin.readline().split())
queue=deque()
result=[]
for i in range(n):
    queue.append(i+1)
    
while len(queue)>1:
    for i in range(k-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())
    #print(f"queue : {queue}")
result.append(queue.popleft())
print("<",end="")
for i in range(n):
    if i==n-1:
        print(f"{result[i]}",end="")
    else:
        print(f"{result[i]}, ",end="")
print(">")

    