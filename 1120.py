str1,str2=input().split()
count = 0
min_count=51

for i in range(len(str2)-len(str1)+1): # i :비교 시작 인덱스
    count = 0
    compare_index=i
    for j in str1:
        if j!=str2[compare_index]:
            count += 1
            #print("차이 if문")
        compare_index+=1
    
    if min_count>count:
        #print("수정")
        min_count=count
        
print(min_count)