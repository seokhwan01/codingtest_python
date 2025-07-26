#2×n 타일링
import sys
dp=[0,1,2]
n=int(sys.stdin.readline().strip())
for i in range(3,n+1):
    dp.append(dp[i-1]+dp[i-2])
print(dp[n]%10007)
# input("종료방지")