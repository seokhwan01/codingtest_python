#나무자르기
import sys

n,m=map(int,sys.stdin.readline().split())
trees=[]
trees=list(map(int,sys.stdin.readline().split()))
trees.sort(reverse=True)
max_tree=trees[0]

def find_result(length):
    total=0
    for tree in trees:
        if tree<=length:
            break
        else:
            total+=tree-length
    if total>=m:
        return True
    else:
        return False



def binary_search():
    start=0
    end=max_tree
    while start<=end:
        mid=(start+end)//2
        
        if find_result(mid): #높이 충족 -> 높이 더 올려보기
            start = mid + 1
        else:#불충족 -> 높이 낮추기
            end = mid - 1
    return end

print(binary_search())
# input("종료방지")