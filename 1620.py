#나는야 포켓몬 마스터 이다솜
import sys
number_doc={}
name_doc={}

n,m=map(int,sys.stdin.readline().split())
for i in range(1,n+1):
    name=sys.stdin.readline().strip()
    number_doc[i]=name
    name_doc[name]=i
for i in range(m):
    command=sys.stdin.readline().strip()

    if command.isdigit():#숫자이면
        print(number_doc[int(command)])
    else:
        print(name_doc[command])