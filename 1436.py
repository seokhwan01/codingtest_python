num = int(input())
count = 0
i=666
while True:
    s=str(i)
    if "666" in s:
        count+=1
        
    if count==num:
        print(i)
        break
    else: 
        i+=1
    
    