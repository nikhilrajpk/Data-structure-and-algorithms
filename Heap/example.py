class MaxHeap:
    def __init__(self,array):
        self.array = array
        self.build_heap()
    
    def build_heap(self):
        endIdx = len(self.array)-1
        parentIdx = self.parent(endIdx)
        for i in range(parentIdx,-1,-1):
            self.shift_down(i,endIdx)
    
    def heap_sort(self):
        endIdx = len(self.array)-1
        while endIdx > 0:
            self.swap(0,endIdx)
            endIdx -= 1
            self.shift_down(0,endIdx)
    
    def shift_down(self,currentIdx,endIdx):
        left_childIdx = self.leftChild(currentIdx)
        while left_childIdx <= endIdx:
            right_childIdx = self.rightChild(currentIdx)
            if right_childIdx <= endIdx and self.array[left_childIdx] < self.array[right_childIdx]:
                largeValIdx = right_childIdx
            else:
                largeValIdx = left_childIdx
            
            if self.array[currentIdx] < self.array[largeValIdx]:
                self.swap(currentIdx,largeValIdx)
            currentIdx = largeValIdx
            left_childIdx = self.leftChild(currentIdx)
        
    def shift_up(self,currentIdx):
        parentIdx = self.parent(currentIdx)
        while parentIdx >= 0 and self.array[parentIdx] < self.array[currentIdx]:
            self.swap(parentIdx,currentIdx)
            currentIdx = parentIdx
            parentIdx = self.parent(currentIdx)
    
    def insert(self,val):
        self.array.append(val)
        endIdx = len(self.array)-1
        self.shift_up(endIdx)
    
    def remove(self):
        endIdx = len(self.array)-1
        self.swap(0,endIdx)
        print(self.array.pop())
        self.shift_down(0,endIdx-1)
        
    def swap(self,leftIdx, rightIdx):
        self.array[leftIdx],self.array[rightIdx] = self.array[rightIdx],self.array[leftIdx]
    
    def parent(self,currentIdx):
        return (currentIdx - 1)//2
    
    def leftChild(self,currentIdx):
        return (2 * currentIdx + 1) 
    
    def rightChild(self,currentIdx):
        return (2 * currentIdx + 2)
    
    def display(self):
        print(self.array)
        
if __name__== '__main__':
    number = [1, 4, 9, 17, 18, 20, 22, 23, 34]
    heap = MaxHeap(number)
    heap.display()
    heap.insert(19)
    heap.display()
    heap.remove()
    heap.display()
    heap.heap_sort()
    heap.display()