#비밀번호 찾기
import sys
result_dict={}

a,b=map(int,sys.stdin.readline().split())
for _ in range(a):
    address,password=map(str,sys.stdin.readline().split())
    result_dict[address]=password
# print(result_dict)

for _ in range(b):
    find_password=sys.stdin.readline().strip()
    #print(find_password)
    if find_password in result_dict:
        print(result_dict[find_password])
    else:
        print("잘못된 주소")

