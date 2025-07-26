#듣보잡
#김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오
import sys
n,m=map(int,sys.stdin.readline().split())
not_listen = []
not_seen = []
for i in range(n):
    name = sys.stdin.readline().strip()
    not_listen.append(name)


for i in range(m):
    name = sys.stdin.readline().strip()
    not_seen.append(name)
not_seen.sort()

not_listen_seen=(set(not_listen) & set(not_seen))
not_listen_seen=sorted(not_listen_seen)
print(len(not_listen_seen))
for i in not_listen_seen:
    print(i)
