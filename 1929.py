import sys
import math
##에라토스테네스의 체 : O(nlogn) 자신은 제외한 배수 거름
#약수 판별은 제곱근 까지만 확인하면 가능함!!
m,n=map(int,sys.stdin.readline().split())
result=[True]*(n+1)
result[1]=False ##1은 소수가 아니므로 False만들고 시작
for i in range(2,int(math.sqrt(n))+1):
    if result[i]:
        j=2
        while i*j<=n:
            result[i*j]=False
            j+=1
for i in range(m,n+1):
    if result[i]:
        print(i)