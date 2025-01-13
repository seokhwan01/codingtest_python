def compare(sub_board):#n,m 비교 시작 인덱스
    count_W, count_B = 0, 0
    W_start_board = ["WBWBWBWB", "BWBWBWBW"] * 4
    B_start_board = ["BWBWBWBW", "WBWBWBWB"] * 4

    for i in range(8):
        for j in range(8):
            if sub_board[i][j] != W_start_board[i][j]:
                count_W += 1
            if sub_board[i][j] != B_start_board[i][j]:
                count_B += 1

    return min(count_W, count_B)
    
n,m=map(int,input().split()) #행 : N , 열 : M
board = [[""]*m for _ in range(n)] #n개 행 m개열 리스트 생성
for i in range(n):
    str = input()
    #print(f"str : {str}")
    for j in range(m):
        board[i][j]=str[j]##인덱스 에러
        
min_num=2501
for i in range(n-7):
    for j in range(m-7):
        #print(f"i : {i}, j : {j}")
        sub_board = [row[j:j+8] for row in board[i:i+8]]
        #print(sub_board)
        num=compare(sub_board)
        #print(f"num : {num}")
        if min_num>num:
            min_num=num
print(min_num)