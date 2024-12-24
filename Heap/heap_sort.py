class Heap_sort:
    def heap_sort(self,array):
        self.array = array
        endIdx = len(self.array)-1
        self.build_tree(endIdx)
        while endIdx > 0:
            self.swap(0,endIdx)
            endIdx -= 1
            self.build_tree(endIdx)
            
        return self.array
    
    def build_tree(self,endIdx):
        parentIdx = self.parent(endIdx)
        for i in range(parentIdx, -1, -1):
            self.shift_down(i,endIdx)
    
    def shift_down(self,parentIdx,endIdx):
        leftChildIdx = self.leftChild(parentIdx)
        while leftChildIdx <= endIdx:
            rightChildIdx = self.rightChild(parentIdx)
            if rightChildIdx <= endIdx and self.array[leftChildIdx] < self.array[rightChildIdx]:
                largeValIdx = rightChildIdx
            else:
                largeValIdx = leftChildIdx
            
            if self.array[parentIdx] < self.array[largeValIdx]:
                self.swap(parentIdx,largeValIdx)
            else:
                return
            parentIdx = largeValIdx
            leftChildIdx = self.leftChild(parentIdx)
    
    def swap(self,leftIdx,rightIdx):
        self.array[leftIdx],self.array[rightIdx] = self.array[rightIdx],self.array[leftIdx]
    
    def parent(self,currentIdx):
        return (currentIdx - 1)//2
    
    def leftChild(self,currentIdx):
        return (2 * currentIdx + 1)
    
    def rightChild(self,currentIdx):
        return (2 * currentIdx + 2)
    
if __name__ == '__main__':
    # array = [10, 5, 25, 3, 30, 22, 12]
    array = [8, 10, 15, 20, 22, 18, 26, 30, 40, 1]
    heap = Heap_sort()
    print(heap.heap_sort(array))