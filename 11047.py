num,total = map(int,input().split()) #동전 종류 갯수, 총 가격
coin_list=[]
for i in range (num):
    coin_list.append(int(input("")))

total_count = 0
count =0

coin_list.sort(reverse=True)
for one_coin in coin_list:
    
    if one_coin <= total:
        count = total // one_coin
        print(f"코인 : {one_coin} , count : {count}")
        total = total%one_coin
        total_count += count
    if total == 0:
        break
        
        
print(total_count)
            
            