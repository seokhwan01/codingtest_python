num = int(input())
stack=[]
for i in range (num):
    x=int(input())
    if x==0:
        stack.pop()
    else:
        stack.append(x)
print(sum(stack))