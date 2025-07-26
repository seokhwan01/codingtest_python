# 1로 만들기
# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
result_dict={
    1:0
}

num = int(input())
for i in range(2,num+1):
    # print(f"i :{i}")
    if i%2==0 and i%3==0:
        result_dict[i]=min(result_dict[i//2]+1,result_dict[i//3]+1)
    elif i%2==0:
        result_dict[i]=min(result_dict[i//2]+1,result_dict[i-1]+1)
    elif i%3==0:
        result_dict[i]=min(result_dict[i//3]+1,result_dict[i-1]+1)
    else:
        result_dict[i]=result_dict[i-1]+1

# print(result_dict)
print(result_dict[num])

