class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        if self.tail is None:
            self.tail = node
    
    
    def insert_at_end(self, data):
        node = Node(data, None)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
       
            
    def insert_values(self, data_list):
        for data in data_list:
            ll.insert_at_end(data)
                 
    def get_length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
    
    def insert_at(self, data, index):
        if not 0 <= index < self.get_length():
            raise Exception('invalid index')
        if index == 0:
            ll.insert_at_beginning(data)
            return
        count = 0
        temp = self.head
        while temp:
            if count == index - 1:
                node = Node(data, temp.next)
                temp.next = node
                if node.next is None:
                    self.tail = node
                return
            temp = temp.next
            count += 1
            
    def remove_from(self, index):
        length = self.get_length()
        if not 0 <= index <= length:
            raise Exception('invalid index')
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return
        count = 0
        temp = self.head
        while temp:
            if count == index - 1 :
                temp.next = temp.next.next
                if temp.next is None:
                    self.tail = temp
                return
            temp = temp.next
            count += 1
            
       
    def insert_after_value(self, data, after_value):
        if self.head is None:
            print('empty')
            return
        if self.tail.data == after_value:
            print('adding at end')
            self.insert_at_end(data)
            return
        temp = self.head
        while temp:
            if temp.data == after_value:
                node = Node(data, temp.next)
                temp.next = node
                return
            temp = temp.next
        print('there is no element:',after_value)
        
    
    def remove_value(self,value):
        if self.head is None:
            print('LL empty')
            return
        if self.head.data == value:
            self.head = self.head.next
            if self.head is None:           # if LL become empty
                self.tail = None
            return
        temp = self.head
        while temp:
            if temp.next and temp.next.data == value:
                temp.next = temp.next.next
                if temp.next is None:
                    self.tail = temp
                return
            temp = temp.next
        print('there is no value : ',value)
        
          
    def reverse(self):
        next_node = None
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            if prev is None:
                self.tail = current
            prev = current
            current = next_node
        self.head = prev
        return
    
    def duplicate(self):
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
        return
            

                
            
    def display(self):
        temp = self.head
        llstr = ''
        while temp:
            llstr += str(temp.data)
            temp = temp.next
            llstr += '-->' if temp else ''
        print(llstr)
        print('head:',self.head.data)
        print('tail:',self.tail.data)
        return
ll = LinkedList()
ll.insert_at_beginning(1)
ll.insert_at_beginning(2)
ll.insert_at_end(3)
ll.insert_at_end(4)
ll.insert_values([1,2,5,5,5,8])
ll.display()
print('length of the LL : ', ll.get_length())
ll.insert_at(10,1)
ll.remove_from(9)
ll.insert_after_value(20,6)
ll.remove_value(5)
ll.reverse()
ll.display()
ll.duplicate()
ll.display()


