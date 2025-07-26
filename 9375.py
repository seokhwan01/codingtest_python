#패션왕 신해빈
import sys
test_case=int(sys.stdin.readline().strip())
for _ in range(test_case):
    clothes={}
    combination_num=int(sys.stdin.readline().strip())

    if combination_num==0:
        print(0)
        continue

    for i in range(combination_num):
        clothes_name,clothes_type=map(str,sys.stdin.readline().split())
        if clothes_type in clothes:
            clothes[clothes_type].append(clothes_name)
        else:
            clothes[clothes_type]=[clothes_name]

    result=1
    for value in clothes.values():
        result*=(len(value)+1)
   
    print(result-1)

# input("종료 방지")