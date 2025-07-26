#직각삼각형
#과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다.
#주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    a, b, c = sorted([a, b, c])
    if a == 0 and b == 0 and c == 0:
        break

    if a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")