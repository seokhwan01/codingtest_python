#push,pop,size,empty,front,back
import sys
from collections import deque
n=int(sys.stdin.readline())
commands=[sys.stdin.readline().strip() for i in range(n)]
queue = deque()

for i in range(n):
    s=commands[i]
    if "push" in s:
        queue.append(s[5:])
    elif s=="pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif s=="size":
        print(len(queue))
    elif s=="empty":
        if queue:
            print(0)
        else:
            print(1)
    elif s=="front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif s=="back":
        if queue:
            print(queue[len(queue)-1])
        else:
            print(-1)
    else:
        print("~~~~~~~error~~~~~~")