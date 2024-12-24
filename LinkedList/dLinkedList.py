class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head, None)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            self.head = node
        # if self.head:
        #     self.head.prev = node
        # self.head = node
        # if self.tail is None:
        #     self.tail = node
        return
    
    def insert_at_end(self, data):
        node = Node(data, None, self.tail)
        if self.tail is None:
            self.head = node
            self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = node
        return
    
    def insert_values(self,data_list):
        for data in data_list:
            self.insert_at_end(data)
        return
    
    def get_length(self):
        temp = self.head
        count = 0
        while temp:
            temp = temp.next
            count +=1 
        return count
    
    def insert_at(self, data, index):
        length = self.get_length()
        if not 0 <= index <= length:
            raise Exception('invalid index')
        if index == 0:
            self.insert_at_beginning(data)
            return
        if index == length:
            self.insert_at_end(data)
            return
        count = 0
        temp = self.head
        while temp:
            if count == index -1 :
                node = Node(data, temp.next, temp.next.prev)
                temp.next = node
                node.next.prev = node
                return
            temp = temp.next
            count += 1
            
    def remove_from(self, index):
        if not self.head:
            print('empty')
            return
        length = self.get_length()
        if not 0 <= index < length:
            raise Exception('invalid index')
        if index == 0:
            self.head = self.head.next
            return
        if index == length-1:
            self.tail = self.tail.prev
            self.tail.next = None
            return
        count = 0
        temp = self.head
        while temp:
            if count == index-1:
                temp.next = temp.next.next
                temp.next.prev = temp.next.prev.prev
                return
            temp = temp.next
            count += 1
            
    
    def insert_after(self, data, value):
        if self.head is None:
            print('empty')
            return
        if self.tail.data == value:
            self.insert_at_end(data)
            return
        temp = self.head
        while temp:
            if temp.data == value:
                node = Node(data, temp.next, temp.next.prev)
                temp.next = node
                node.next.prev = node
                return
            temp = temp.next
        print('no such element')
        
    
    def remove(self, value):
        if self.head is None:
            print('empty')
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        if self.tail.data == value:
            self.tail = self.tail.prev
            return
        temp = self.head
        while temp:
            if temp.next and temp.next.data == value:
                temp.next = temp.next.next
                temp.next.prev = temp
                return
            temp = temp.next
        print('no such value')
        
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
        temp = self.head
        llstr = ''
        while temp:
            llstr += str(temp.data)
            temp = temp.next
            llstr += '<-->' if temp else ''
            if temp and temp.prev : print('prev is : ', temp.prev.data)
        print(llstr)
        print('head',self.head.data,'tail', self.tail.data) if self.head and self.tail else print()
        
        back = self.tail
        bstr=''
        while back:
            bstr += str(back.data)
            back = back.prev
            if back : bstr += '<-->'
        print(bstr)
        # print('head',self.head.data,'tail', self.tail.data) if self.head and self.tail else print()

ll = DLinkedList()
# ll.insert_at_beginning(1)
# ll.insert_at_beginning(2)
# ll.insert_at_beginning(3)


# ll.insert_at_end(4)
# ll.insert_at_end(5)
# ll.insert_at_end(6)

ll.insert_values([1,2,3,4,5])

print('length : ', ll.get_length())

# n = int(input('enter the index:'))

# ll.insert_at(6,n)

# ll.remove_from(0)
# ll.remove_from(0)
# ll.remove_from(0)
# ll.remove_from(0)
# ll.remove_from(0)

# ll.insert_after(6,2)

# ll.remove(1)
# ll.remove(2)
# ll.remove(3)
# ll.remove(4)
# ll.remove(5)

ll.reverse()

ll.display()            