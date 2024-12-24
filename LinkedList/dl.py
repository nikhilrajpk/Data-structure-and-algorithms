class Node:
    def __init__(self,prev,data,next):
        self.prev = prev
        self.data = data
        self.next = next
class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_at_beginning(self,data):
        node = Node(None,data,self.head)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            self.head = node
        return
    def insert_at_end(self,data):
        node = Node(self.tail,data,None)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        return
    def insert_values(self, data_list):
        for data in data_list:
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
        if not 0 <= index <= self.get_length():
            raise Exception('invalid index.')
        if index == 0:
            self.insert_at_beginning(data)
            return
        if index == self.get_length():
            self.insert_at_end(data)
            return
        temp = self.head
        count = 0
        while temp:
            if count == index-1:
                node = Node(temp,data,temp.next)
                temp.next = node
                node.next.prev = node
                return
            temp = temp.next
            count += 1
    def remove_from_index(self,index):
        if not 0<= index < self.get_length():
            raise Exception('invalid index')
        if index == 0:
            self.head = self.head.next
            return
        if index == self.get_length()-1:
            self.tail = self.tail.prev
            self.tail.next = None
            return
        temp = self.head
        count = 0
        while temp:
            if count == index-1:
                temp.next = temp.next.next
                temp.next.prev = temp
                return
            temp = temp.next
            count += 1
    def insert_after(self,data,value):
        if self.head is None:
            print('empty')
            return
        if self.tail.data == value:
            self.insert_at_end(data)
            return
        temp = self.head
        while temp:
            if temp.data == value:
                node = Node(temp,data,temp.next)
                temp.next = node
                node.next.prev = node
                return
            temp = temp.next
        print('no value')
    def remove(self,value):
        if self.head is None:
            print('empty')
            return
        if self.head.data == value:
            self.head = self.head.next
            self.head.prev = None
            return
        if self.tail.data == value:
            self.tail = self.tail.prev
            self.tail.next = None
            return
        temp = self.head
        while temp:
            if temp.next and temp.next.data == value:
                temp.next = temp.next.next
                temp.next.prev = temp
                return
            temp = temp.next
        print('no value')
    def duplicate(self):
        if self.head is None:
            print('empty')
            return
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
        current = self.head
        while current:
            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = temp
        self.head, self.tail = self.tail, self.head
    
    
            
    
    def display(self):
        if self.head is None:
            print('empty')
            return
        llstr = []
        temp = self.head
        while temp:
            llstr.append(str(temp.data))
            temp = temp.next
            if temp : llstr.append('<-->')
        print(''.join(llstr))
        print('head:',self.head.data,'   tail:',self.tail.data)
        
        rev = self.tail
        r = []
        while rev:
            r.append(str(rev.data))
            rev = rev.prev
            if rev : r.append('<-->')
        print(''.join(r))
        return
    
ll = DLinkedList()

ll.insert_at_beginning(2)
ll.insert_at_beginning(1)
ll.insert_at_end(3)
ll.insert_values([4,5,6,7])
print('length:',ll.get_length())
# ll.insert_at_index(99,1)
# ll.remove_from_index(1)
# ll.insert_after(99,6)
# ll.remove(1)
# ll.display()
# ll.duplicate()
# ll.reverse()
ll.display()