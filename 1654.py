#랜선 자르기
import sys
def line_count(n):
    current_max=line_list[-1]
    current_min=1
    result=0

    while current_min <= current_max:
        mid=(current_max+current_min)//2
        count = sum(line // mid for line in line_list)

        if count>=n:
            result=mid
            current_min=mid+1
        else:
            current_max=mid-1
        
    print(result)
    # input("종료방지")
    
k,n=map(int,sys.stdin.readline().split())
line_list=[]
one_flag=True
for _ in range(k):
    x=int(sys.stdin.readline().strip())
    line_list.append(x)
    if x!=1:
        one_flag=False
if one_flag:
    print(1)
    exit()
if k==1 and n==1:
    print(line_list[0])
    exit()
else:
    line_list.sort()
    line_count(n)
