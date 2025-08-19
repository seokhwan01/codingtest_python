#Four Squares x 
#모든 제곱수 j*j에 대해 i-j*j만들기
#python3 시간초과 pypy3로 제출 후 성공
import sys
n=int(sys.stdin.readline().strip())
dp=[0]*(n+1)

for i in range(1,n+1):
    dp[i]=i
    j=1
    while j*j<=i:
        dp[i]=min(dp[i],dp[i-j*j]+1)
        j+=1

print(dp[n])
# input("대기")