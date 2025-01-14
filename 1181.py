num=int(input())
result = []
for i in range(num):
    input_str = input()
    if input_str not in result:
        result.append(input_str)
        #print("삽입 완료")
    
result.sort(key=lambda x: (len(x), x))#길이 순 정렬 -> 같으면 사전 순
# "apple"  -> (5, "apple")
# "banana" -> (6, "banana")
# "kiwi"   -> (4, "kiwi")
# "pear"   -> (4, "pear")
# "berry"  -> (5, "berry")
for i in result:
    print(i)