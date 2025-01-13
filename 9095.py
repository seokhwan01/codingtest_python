# i>=4 일대 dp[n]=dp[n-1]+dp[n-2]+dp[n-3]
#n-1에서 1 더하기 : n-1 만드는 경우의 수와 동일
#n-2에서 2 더하기 : n-2 만드는 경우의 수와 동일
#n-3에서 3 더하기 : n-3 만드는 경우의 수와 동일
num= int(input())
result = []
for i in range(num):
    n=int(input())
    dp = [0]*(n+1)
    
    for j in range(1,n+1):
        if j==1:
            dp[j]=1
        elif j==2:
            dp[j]=2
        elif j==3:
            dp[j]=4
        else:
            dp[j]=dp[j-1]+dp[j-2]+dp[j-3]
            
    result.append(dp[j])
for i in result:
    print(i,end=" ")