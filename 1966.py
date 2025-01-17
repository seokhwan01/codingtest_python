#백준 1966번: 프린터 큐
import sys
from collections import deque

num=int(sys.stdin.readline())
result =[]

for i in range(num):
    queue=deque()
    n,m=map(int,sys.stdin.readline().split()) #n은 큐의 갯수 ,m은 찾을 인덱스
    score=list(map(int,sys.stdin.readline().split()))
    
    for i in range(n):   
        queue.append((score[i],i)) #값과 인덱스를 큐에 삽입 m이 인덱스와 일치하면 뽑아냄
        
    count=0
    while True:
        if queue[0][0]==max(queue, key=lambda x: x[0])[0]: #맨 앞이 최대이면
            if queue[0][1]==m:
                result.append(count+1)
                break
            else:
                queue.popleft()
                count+=1
        else:
            queue.append(queue.popleft())
for i in result:
    print(i)
            
        
    