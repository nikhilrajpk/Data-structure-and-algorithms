class Heap:
    def __init__(self,array):
        self.array = array
        self.build_tree()
        
    def build_tree(self):
        endIdx = len(self.array)-1
        lastParentIdx = self.parent(endIdx)
        for i in range(lastParentIdx,-1,-1):
            self.shift_down(i)
            
    def shift_down(self,currentIdx):
        endIdx = len(self.array)-1
        left_child_idx = self.leftChild(currentIdx)
        while left_child_idx <= endIdx:
            right_child_idx = self.rightChild(currentIdx)
            if right_child_idx <= endIdx and self.array[left_child_idx] > self.array[right_child_idx]:
                small_val_idx = right_child_idx
            else:
                small_val_idx = left_child_idx
            
            if self.array[currentIdx] > self.array[small_val_idx]:
                self.array[currentIdx],self.array[small_val_idx] = self.array[small_val_idx],self.array[currentIdx]
            else:
                return
            currentIdx = small_val_idx
            left_child_idx = self.leftChild(left_child_idx)
            
    def shift_up(self,currentIdx):
        parentIdx = self.parent(currentIdx)
        while parentIdx >= 0 and self.array[parentIdx] > self.array[currentIdx]:
            self.array[parentIdx],self.array[currentIdx] = self.array[currentIdx],self.array[parentIdx]
            currentIdx = parentIdx
            parentIdx = self.parent(currentIdx)
    
    def insert(self,value):
        self.array.append(value)
        currentIdx = len(self.array)-1
        self.shift_up(currentIdx)
    
    def peek(self):
        return self.array[0]
        
    def remove(self):
        endIdx = len(self.array)-1
        self.array[0],self.array[endIdx] = self.array[endIdx],self.array[0]
        root = self.array.pop()
        self.shift_down(0)
        return root
    
    def parent(self,currentIdx):
        parentIdx = (currentIdx - 1) // 2
        return parentIdx
    
    def leftChild(self,currentIdx):
        leftChildIdx = 2 * currentIdx + 1
        return leftChildIdx
    
    def rightChild(self,currentIdx):
        rightChildIdx = 2 * currentIdx + 2
        return rightChildIdx
    
    def display(self):
        print(self.array)
        
if __name__ == '__main__':
    # array = [10, 5, 25, 3, 30, 22, 12]
    array = [8, 10, 15, 20, 22, 18, 26, 30, 40]
    heap = Heap(array)
    heap.display()
    heap.insert(1)
    print('after insering element')
    heap.display()
    print('removing root : ',heap.remove())
    heap.display()
    print('root element : ',heap.peek())