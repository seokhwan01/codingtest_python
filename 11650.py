num = int(input())
arr=[]
for i in range(num):
    a = list(map(int,input().split()))
    arr.append(a)
    
arr.sort(key=lambda x : (x[0],x[1]))
for i in range(num):
    print(f"{arr[i][0]} {arr[i][1]}")