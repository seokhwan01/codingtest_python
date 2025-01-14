num = int(input())
people=[]

for i in range(num):
    people.append(list(map(int,input().split())))
rank_list=[0]*num
##덩치 클 때 작을 때만 구분!!
for i in range(num):
    rank=num
    for j in range(num):
        if i==j:
            continue
        if people[i][0]>people[j][0] and people[i][1]>people[j][1]:#덩치가 더 큼
            rank-=1
        
        elif people[i][0]<people[j][0] and people[i][1]<people[j][1]:#덩치 더 작음
            pass
            #print(f"people[i] : {people[i]}, people[j] : {people[j]}")
        else:#비교 불가면
            rank-=1
        
        rank_list[i]=rank
for i in rank_list:
    print(i,end=" ")