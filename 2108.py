import sys
from collections import Counter
# def round_half(num):
#     if num<0:
#         if int(num)-num>=0.5:
#             return int(num)-1
#         else:
#             return int(num)
#     if num-int(num)>=0.5:
#         return int(num)+1
#     else:
#         return int(num)
n=int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
#print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

#산술평균
i=sum(arr)/n
print(round(i))
#중앙값
temp_arr=arr[:]
temp_arr.sort()
print(temp_arr[n//2])

#최빈값 N^2에서 시간 초과 발생
dic=dict()
for i in arr:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
f_max=max(dic.values())
frequence_max=[]
for i in dic:
    if f_max==dic[i]:
        frequence_max.append(i)
if len(frequence_max)==1:
    print(frequence_max[0])
else:
    print(frequence_max[1])
        
#해결 방안? : Counter사용 : 딕셔너리 형식으로 빈도수 저장해줌
# frequence=Counter(arr)
# frequence=list(frequence.items())
# #print(frequence)
# frequence.sort(key=lambda x : (-x[1],x[0])) ##x[1] 비교는 내림차순이므로 -x[1]!!
# print(frequence)
# if len(frequence)==1:
#     print(frequence[0][0])
# else:
#     if frequence[0][1]==frequence[1][1]:
#         print(frequence[1][0])
#     else:
#         print(frequence[0][0])

#범위 (최대 - 최소)
print(max(arr)-min(arr))