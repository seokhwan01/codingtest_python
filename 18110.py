import sys
from collections import deque
##파이썬 round함수는 이상하므로 직접 만들어 사용
def round_fun(num):
    if num-int(num) >= 0.5:
        return int(num)+1
    else:
        return int(num)
n = int(input())

if n==0:
    print(0)
    exit()
score=deque()
adjust_factor=round_fun((n*15)/100)
#print(adjust_factor)
for i in range(n):
    score.append(int(sys.stdin.readline()))
score.sort()
for i in range(adjust_factor):
    score.pop()
    score.popleft()
print(round_fun(sum(score)/len(score)))