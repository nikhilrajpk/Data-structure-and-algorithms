class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.head = node
    
    def insert_at_end(self,data):
        node = Node(data,None)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def insert_values(self, datalist):
        for data in datalist:
            self.insert_at_end(data)
        return
    
    def get_length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
    
    def insert_at_index(self,data,index):
        if self.head is None:
            print('empty')
            return
        n = self.get_length()
        if not 0 <= index <= n:
            raise Exception('invalid index')
        if index == 0:
            print('inserting at the beginning')
            self.insert_at_beginning(data)
            return
        if index == n:
            print('inserting at the end')
            self.insert_at_end(data)
            return
        temp = self.head
        count = 0
        while temp:
            if count == index-1:
                node = Node(data,temp.next)
                temp.next = node
                return
            temp = temp.next
            count += 1
            
    def remove_from_index(self,index):
        if self.head is None:
            print('empty')
            return
        if not 0<= index <=self.get_length():
            raise Exception('invalid index.')
        if index == 0:
            print('removing the head.')
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            print(self.tail)
            return
        temp = self.head
        count = 0
        while temp:
            if count == index-1:
                temp.next = temp.next.next
                if temp.next is None:
                    self.tail = temp
                return
            temp = temp.next
            count += 1
    
    def insert_after(self,data,value):
        if self.head is None:
            print('empty list')
            return
        if self.tail.data == value:
            node = Node(data,None)
            self.tail.next = node
            self.tail = node
            print('tail:',self.tail.data)
            return
        temp = self.head
        while temp:
            if temp.data == value:
                node = Node(data,temp.next)
                temp.next = node
                return
            temp = temp.next
        print('No value found.')
        return -1
    
    def remove(self,value):
        if self.head is None:
            print('empty list')
            return
        if self.head.data == value:
            print('removing head')
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return
        temp = self.head
        while temp :
            if temp.next and temp.next.data == value:
                temp.next = temp.next.next
                print('tail before:',self.tail)
                if temp.next is None:
                    self.tail = temp
                    print('tail after:',self.tail)
                return
            temp = temp.next
        print('no value')
        
    def duplicate(self):
        if self.head is None:
            print('empty')
            return                         # [1,2,2,2,3,4,5,4]
        current = self.head
        while current:
            n = current.next
            if n and current.data == n.data:
                while n and current.data == n.data:
                    n = n.next
                current.next = n
                if current.next is None:
                    self.tail = current
            current = current.next
            
    def reverse(self):
        prev = None
        current = self.head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head, self.tail = self.tail, self.head
        print('head:',self.head.data, 'tail:',self.tail.data)
    
    
    def display(self):
        if self.head is None:
            print('empty')
            return
        temp = self.head
        # n = self.get_length()
        llstr = []
        while temp:
            llstr.append(str(temp.data))
            temp = temp.next
            if temp: llstr.append('-->')
        print(''.join(llstr))
        return
    
ll = LinkedList()
# ll.insert_at_beginning(1)
# ll.insert_at_beginning(2)

# ll.insert_at_end(3)

ll.insert_values([1,2,3,4])

# ll.insert_at_index(5,5)
# ll.remove_from_index(7)

# ll.insert_after(2,4)
# ll.remove(5)

# ll.duplicate()

ll.reverse()
ll.display()