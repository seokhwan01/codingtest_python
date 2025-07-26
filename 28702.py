# #FizzBuzz 
# FizzBuzz 문제는 
# $i = 1, 2, \cdots$ 에 대해 다음 규칙에 따라 문자열을 한 줄에 하나씩 출력하는 문제입니다.
# $i$가 
# $3$의 배수이면서 
# $5$의 배수이면 “FizzBuzz”를 출력합니다.
# $i$가 
# $3$의 배수이지만 
# $5$의 배수가 아니면 “Fizz”를 출력합니다.
# $i$가 
# $3$의 배수가 아니지만 
# $5$의 배수이면 “Buzz”를 출력합니다.
# $i$가 
# $3$의 배수도 아니고 
# $5$의 배수도 아닌 경우 
# $i$를 그대로 출력합니다.
# FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열이 주어집니다. 이때, 이 세 문자열 다음에 올 문자열은 무엇일까요?

#isdigit() : 문자열이 정수로만 이루어졌을 때 ("123")
import sys
count = 0

for i in range(3):
    a = sys.stdin.readline().strip()
    #print(f"a : {a}")
    if a.isdigit(): #숫자이면
        #print("정수")
        count = int(a)+1
    else:
        count+=1

#print(f" count : {count}")
if count%3==0 and count%5==0:
    print("FizzBuzz")
elif count%3==0 and count%5!=0:
    print("Fizz")
elif count % 3 !=0 and count %5 == 0:
    print("Buzz")
else:
    print(count)