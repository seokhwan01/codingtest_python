#색종이 만들기
    
import sys
n=int(sys.stdin.readline().strip())
arr = []

white_count=0
blue_count=0

for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    arr.append(row)

def count(size,x,y):
    global white_count
    global blue_count
    color=arr[x][y]
    flag=True

    for i in range(x,x+size):
        for j in range(y,y+size):
            if color==arr[i][j]:
                pass
            else:
                flag=False
    if flag:
        if color==1:
            blue_count+=1
        else:
            white_count+=1
        return
    else:
        count(size//2, x, y)
        count(size//2, x+size//2, y)
        count(size//2, x, y+size//2)
        count(size//2, x+size//2, y+size//2)

count(n,0,0)
print(white_count)
print(blue_count)