#유기농 배추
import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 제한 해제

def dfs(x,y):
    if x<0 or x>=m or y<0 or y>=n:
        return
    if field[x][y]==0:
        return
    field[x][y]=0

    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)

test_num=int(sys.stdin.readline().strip())
for _ in range(test_num):
    m,n,k=map(int,sys.stdin.readline().split())
    field= [[0 for _ in range(n)] for _ in range(m)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        field[x][y] = 1

    count=0
    for i in range(m):
        for j in range(n):
            if field[i][j]==1:
                dfs(i,j)
                count += 1
    print(count)
    
# input("종료방지")

