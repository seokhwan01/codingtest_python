#백준 1920 : 수 찾기
n=int(input())
arr=list(map(int,input().split()))
dict = {key:None for key in arr}
m=int(input())
find_arr=list(map(int,input().split()))
for i in find_arr:
    if i in dict:
        print(1)
    else:
        print(0)