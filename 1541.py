def parsing_fun(input_str):
    global const_list_len
    global operator_list_num
    
    check_num =["0","1","2","3","4","5","6","7","8","9"]
    check_operator = ["+","-"]
    num_element = ""

    const_list = [] #정수 리스트
    operator_list=[] # 기호 리스트

    flag = 0 #1은 기호 뒤에 0바로 나오는거 처리
    for i in range(len(input_str)):
        if input_str[i] in check_num: #숫자 처리
            if flag==1 and input_str[i]=="0":
                continue
            
            flag=0
            num_element += input_str[i]
            #print(f"if문 들옴 : {input_str[i]}, num_element : {num_element}")
            if i < len(input_str)-1 and input_str[i+1] in check_operator:
                const_list.append(int(num_element))
                num_element=""
            elif i == len(input_str)-1:
                const_list.append(int(num_element))
                num_element=""
            
        elif input_str[i] in check_operator: #기호     
            operator_list.append(input_str[i])
            flag = 1
    const_list_len=len(const_list)
    operator_list_num=len(operator_list)
    
    return const_list+operator_list
    #숫자 기호 리스트 처리 완료

# -일때 + 나올때 까지 묶어 최대로 만든 값을 빼자
# 숫자와 기호 각각 나눠 리스트형 저장
if __name__ == '__main__':
    const_list_len=0
    operator_list_num=0    
    input_str = input()
    result_list = parsing_fun(input_str)
    const_list,operator_list=result_list[:const_list_len],result_list[const_list_len:]
    #print(f"상수 : {const_list}, 기호 : {operator_list}")
    
    minus_index =[]
    ### - 인덱스 찾기
    for i in range(operator_list_num):
        if operator_list[i] == "-":
            minus_index.append(i)
    #print(f"-인덱스  {minus_index}")
    
    part_total = 0
    part_total_list = []
    total = 0
    ### +끼리만 합치기
    for i in range(const_list_len):
        if i not in minus_index:
            part_total += const_list[i]
            if i==const_list_len-1:
                part_total_list.append(part_total)
        else:
            part_total += const_list[i]
            part_total_list.append(part_total)
            part_total=0
    #print(f"part_total_list : {part_total_list}") 
       
    for i in range(len(part_total_list)):
        if i ==0:
            total+=part_total_list[i]
        else:
            total -=part_total_list[i]
    print(total)
    


