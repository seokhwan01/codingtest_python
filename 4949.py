#백준 4949번, 균형잡힌 세상
sentences=[]
stack=[]
while True:
    s=input()
    if s==".":
        break
    sentences.append(s)
#print(sentences)
for sentence in sentences:
    flag=0 #0은 정상 1은 오류
    stack.clear()
    for char in sentence:
        if char=="[": #[은 넣고 ]은빼기
            stack.append("[")
        elif char=="]":
            if stack:
                if stack.pop()!="[":
                    flag=1
                    break
            else:
                flag=1
                break
                         
        elif char=="(":
            stack.append("(")
        elif char==")" :
            if stack:
                if stack.pop()!="(":
                    flag=1
                    break
            else:
                flag=1
                break    

    if len(stack)==0 and flag==0:
        print("yes")
    else:
        print("no")