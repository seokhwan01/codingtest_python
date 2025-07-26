#피보나치 함수
#fibonachi(0)은 0출력
#fibonachi(1)은 1출력
#0과 1이 몇번 출력되는지
import sys

fibonachi_dict={0 : [1,0],
                1 : [0,1]}
def fibonachi(n):
    if n in fibonachi_dict:
        return fibonachi_dict[n]

    else:
        count1=fibonachi(n-1)
        count2=fibonachi(n-2)
        fibonachi_dict[n]=[count1[0]+count2[0],count1[1]+count2[1]]
        return fibonachi_dict[n]


num = int(sys.stdin.readline().strip())

for i in range(num):

    fibonachi_num = int(sys.stdin.readline().strip())
    result = fibonachi(fibonachi_num)
    print(f"{result[0]} {result[1]}")
