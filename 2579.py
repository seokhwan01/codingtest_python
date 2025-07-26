#계단 오르기
import sys

n=int(sys.stdin.readline().strip())
stairs_score=[0]
for i in range(1,n+1):
    score=int(sys.stdin.readline().strip())
    stairs_score.append(score)
if n==0:
    print(0)
    exit()
if n==1:
    print(stairs_score[1])
    exit()
if n==2:
    print(stairs_score[1]+stairs_score[2])
    exit()


dp=[0]*(n+1)
dp[1]=stairs_score[1]
dp[2]=stairs_score[1]+stairs_score[2]

for i in range(3,n+1):
    dp[i]=max(dp[i-2],dp[i-3]+stairs_score[i-1])+stairs_score[i]
# print(dp)
print(dp[n])