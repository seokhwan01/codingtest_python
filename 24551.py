from collections import deque
n= int(input()) # n : 자료구조의 갯수
queuestack_status=list(map(int,input().split()))#0은 큐, 1은 스택
queuestack=list(map(int,input().split()))
m=int(input())
insert_list=list(map(int,input().split()))

queue = deque()
##시간 초과 O(nlogn)안에서 해결 방안 찾기
#맨 마지막 큐에 있는 값
#덱 이용해서  스택 무시하고 진행

for i in range(n):
    if queuestack_status[i]==0:
        queue.appendleft(queuestack[i])
        
if not queue:
    for i in insert_list:
        print(i,end=" ")
    exit()
    
for i in range(m):
    queue.append(insert_list[i])
    print(queue.popleft(),end=" ")

    

        
        
                 