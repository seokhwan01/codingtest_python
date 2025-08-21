#최대힙
#힙 직접 구현

class MaxHeap:
    def __init__(self):
        self.heap=[None]
        self.count=0

    def isEmpty(self):
        return self.count == 0
    
    def add_heap(self, value):
        self.heap.append(value)
        self.count+=1

        i=self.count
        #부모와 비교하면서 하나씩 올라감

        while i!=1 and value > self.heap[i//2]:#새로 삽입한 값이 부모보다 크면 → 부모 자리를 끌어내리고 위로 올라감
            self.heap[i]=self.heap[i//2]
            i=i//2
        self.heap[i]=value

    def del_heap(self):
        if self.count==0: #비워 잇으면
            return 0
        
        value=self.heap[1]
        temp=self.heap[self.count]
        self.heap.pop()
        self.count-=1

        parent=1
        child=2
        while child<=self.count:
            if child < self.count and self.heap[child] < self.heap[child+1]:
                child+=1
            if temp >= self.heap[child]:
                break
            
            self.heap[parent] = self.heap[child]
            parent=child
            child*=2
        
        if self.count > 0:
            self.heap[parent] = temp
        
        return value
    
import sys
hp=MaxHeap()

n=int(sys.stdin.readline().strip())
# print("------------------")
for _ in range(n):
    m=int(sys.stdin.readline().strip())

    if m==0:
        print(hp.del_heap())
    else:
        hp.add_heap(m)

# input("종료방지")