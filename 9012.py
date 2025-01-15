n= int(input())
sentences=[]
for i in range(n):
    s=input()
    sentences.append(s)
for sentence in sentences:
    stack=[]
    flag=0#0은 yes 1은 no
    for char in sentence:
        if char =="(":
            stack.append("(")
        elif char==")":
            if stack:
                stack.pop()
            else:
                flag=1
                break
    if len(stack)==0 and flag==0:
        print("YES")
    else:
        print("NO")