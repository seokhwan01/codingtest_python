#백준 2839 : 설탈 배달
dp=[-1]*5001
dp[3]=1
dp[5]=1
num=int(input())
for i in range(6,num+1):
    if dp[i-3]!=-1: #안에 -1인 아닌 값이 들어 있으면
        if dp[i]==-1:
            dp[i]=dp[i-3]+1
        else:
            dp[i] = min(dp[i], dp[i - 3] + 1)
        #print(f"3::i={i}, dp[i]={dp[i]}")
    if dp[i-5]!=-1:
        if dp[i]==-1:
            dp[i]=dp[i-5]+1
        else:
            dp[i] = min(dp[i], dp[i - 5] + 1)
        #print(f"5::i={i}, dp[i]={dp[i]}")
print(dp[num])

##그리디 사용
# n=int(input())
# count=0
# while n>=0:
#     if n%5==0:
#         count+=n//5
#         print(count)
#         exit()
#     n-=3
#     count+=1
# if n<0:
#     print(-1)
# else:
#     print(count)