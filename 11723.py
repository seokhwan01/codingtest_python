#집합
import sys
m=int(sys.stdin.readline().strip())
result={}
check=[]
for _ in range(m):
    command=list(map(str,sys.stdin.readline().split()))
    if len(command) == 2:
        command[1] = int(command[1])

    if command[0]=="add":
        result[command[1]]=0

    elif command[0]=="check":
        # print(result)
        # print(f"command[1]={command[1]}")
        if command[1] in result:
            print(1)
            check.append(1)
        else:
            print(0)
            # check.append(0)
        # print(check)
    elif command[0]=="remove":
        if command[1] in result:
            del result[command[1]]
        else:
            pass
    elif command[0]=="toggle":
        if command[1] in result:
            del result[command[1]]
        else:
            result[command[1]]=0
    elif command[0]=="all":
        result={
            1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0}
    elif command[0]=="empty":
        result={
        }
    else:
        print("command error")
# print(check)