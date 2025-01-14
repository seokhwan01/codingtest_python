def fac(i):
    if i==1:
        return 1
    else:
        return fac(i-1)*i
    
num=int(input())
if num==0:
    print("0")
    exit()
string=str(fac(num))[::-1]#문자열 뒤집기

count = 0
for i in string:
    if i=="0":
        count+=1
    else:
        break
print(count)