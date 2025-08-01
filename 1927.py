#최소 힙
#직접 구현
class Heap:
    def __init__(self,size):
        self.size=size
        self.heap=[None]*(size+1)
        self.count=0

    def isEmpty(self):
        return self.count == 0
    def isFull(self):
        return self.size-1==self.count
    
    def add_heap(self,item):
        if self.isFull():
            return
        self.count+=1
        i=self.count
        while i!=1 and item<self.heap[i//2]:
            self.heap[i]=self.heap[i//2]
            i//=2
        self.heap[i]=item
        # print(item,end=" ")
        # print(self.heap)
    def del_heap(self):
        if self.count==0:
            # print(0)
            return 0
        item=self.heap[1]
        temp=self.heap[self.count]
        self.heap[self.count]=None
        self.count-=1

        parent=1
        child=2

        while child<=self.count:
            if child < self.count and self.heap[child] > self.heap[child+1]:
                child+=1
            if temp<=self.heap[child]:
                break
            self.heap[parent]=self.heap[child]
            parent=child
            child*=2

        if self.count!=0:
            self.heap[parent]=temp
        # print(item)
        # print(f"return {item}")
        return item
        

import sys
n=int(sys.stdin.readline().strip())
hp=Heap(n)
result=[]
for i in range(n):
    x=int(sys.stdin.readline().strip())
    if x==0:
        # print("x==0")
        result.append(hp.del_heap())
    else:
        hp.add_heap(x)
for i in result:
    print(i)