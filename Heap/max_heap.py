class MaxHeap:
    def __init__(self,array):
        self.array = array
        self.build_tree()
        
    def build_tree(self):
        endIdx = len(self.array)-1
        parentIdx = self.parent(endIdx)
        for i in range(parentIdx,-1,-1):
            self.shift_down(i)
    
    def shift_down(self,currentIdx):
        leftChildIdx = self.leftChild(currentIdx)
        endIdx = len(self.array)-1
        while leftChildIdx <= endIdx:
            rightChildIdx = self.rightChild(currentIdx)
            if rightChildIdx <= endIdx and self.array[leftChildIdx] < self.array[rightChildIdx]:
                largeValIdx = rightChildIdx
            else:
                largeValIdx = leftChildIdx
            
            if self.array[currentIdx] < self.array[largeValIdx]:
                self.swap(currentIdx,largeValIdx)
            else:
                return
            
            currentIdx = largeValIdx
            leftChildIdx = self.leftChild(currentIdx)
    
    def shift_up(self,currentIdx):
        parentIdx = self.parent(currentIdx)
        while parentIdx >= 0 and self.array[parentIdx] < self.array[currentIdx] :
            self.swap(parentIdx,currentIdx)
            currentIdx = parentIdx
            parentIdx = self.parent(currentIdx)
    
    def swap(self, leftIdx, rightIdx):
        self.array[leftIdx], self.array[rightIdx] = self.array[rightIdx], self.array[leftIdx]
        
    def insert(self,value):
        self.array.append(value)
        endIdx = len(self.array)-1
        self.shift_up(endIdx)
    
    def remove(self):
        endIdx = len(self.array)-1
        self.swap(0,endIdx)
        root = self.array.pop()
        self.shift_down(0)
    
    def display(self):
        print(self.array)
    
    def parent(self,currentIdx):
        return (currentIdx - 1)//2
    
    def leftChild(self,currentIdx):
        return (2 * currentIdx + 1)
    
    def rightChild(self,currentIdx):
        return (2 * currentIdx + 2)
    
if __name__ == '__main__':
    array = [10, 5, 25, 3, 30, 22, 12]
    heap = MaxHeap(array)
    heap.display()
    heap.insert(29)
    heap.remove()
    heap.display()
    