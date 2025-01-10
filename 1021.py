
# 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
# 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
# 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.\
from collections import deque
n,m=map(int,input().split())
d =deque()
for i in range (n):
    d.append(i+1)

index_list=list(map(int,input().split()))
count=0 
for i in index_list:
    while True:
        if d[0]==i:
            d.popleft()
            break
        else:
            if d.index(i)<len(d)/2: #덱에서 절반 중 왼쪽이면
                while d[0] != i: #첫 인덱스가 찾는 수 일 때 까지
                    d.append(d.popleft()) #덱 왼쪽에서 빼서 오른쪽 삽입
                    count += 1
            else:
                while d[0] != i:
                    d.appendleft(d.pop()) #덱 오른쪽에서 빼서 왼쪽 삽입
                    count+=1
print(count)

    

