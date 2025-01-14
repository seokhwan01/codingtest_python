num = int(input())
people=[]
for i in range(num):
    input_list=input().split()
    input_list.append(i)
    people.append(input_list)
people.sort(key=lambda x : (int(x[0]),int(x[2])))

for i in range(num):
    print(f"{int(people[i][0])} {people[i][1]}")