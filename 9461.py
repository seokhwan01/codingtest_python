#파도반 수열
import sys
dp=[0,1,1,1,2,2]
n=int(sys.stdin.readline().strip())

for _ in range(n):
    T=int(sys.stdin.readline().strip())
    if len(dp)-1<T:
        for i in range(len(dp),T+1):
            dp.append(dp[i-1]+dp[i-5])
            
            # print(f"dp[{i}]={dp[i-1]}+{dp[i-5]}, dp[{i-1}] : {dp[i-1]}, dp[{i-5}]={dp[i-5]}")
    # print(f"dp : {dp}")
    print(dp[T])
# input("엔터를 눌러 종료")  # 종료 방지