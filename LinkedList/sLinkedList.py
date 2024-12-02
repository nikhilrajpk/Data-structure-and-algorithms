# class to create new Node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# class for making operations in Linked list
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Inserting element at beginning
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
    
    # Inserting element at end
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data, None)
    
    # Inserting list of values in the end
    def insert_values(self, data_list):
        for data in data_list:
            ll.insert_at_end(data)
    
    # To get the length of the Linked list
    def get_length(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        print('length of the Linked list : ', count)
        return count
    
    # To insert element at given position
    def insert_at(self, data, index):
        if not 0 <= index < ll.get_length():
            raise Exception('invalid index.')
        if index == 0:
            ll.insert_at_beginning(data)
            return
        count = 0
        temp = self.head
        while temp:
            if count == index - 1:
                node = Node(data, temp.next)
                temp.next = node
                return
            temp = temp.next
            count += 1
            
    # To delete element from given position
    def remove_at(self, index):
        if not 0 <= index < ll.get_length():
            raise Exception("invalid index.")
        if index == 0:
            print('removing head : ', self.head.data)
            self.head = self.head.next
            return
        count = 0
        temp = self.head
        while temp:
            if count == index - 1:
                temp.next = temp.next.next
                return
            temp = temp.next
            count += 1
        
    # To insert data after a value
    def insert_after_value(self, data_to_insert, data_after):
        if self.head is None:
            self.head = Node(data_to_insert, None)
            return
        temp = self.head
        while temp:
            if temp.data == data_after:
                node = Node(data_to_insert, temp.next)
                temp.next = node
                return
            temp = temp.next
        print('There is no value : ', data_after)
        
    # remove the value
    def remove_value(self, data):
        if self.head is None:
            print('The linked list is empty.')
            return
        if self.head.data == data:
            print('removing head : ', self.head.data)
            self.head = self.head.next
            return
        temp = self.head
        while temp:
            if temp.next and temp.next.data == data:
                temp.next = temp.next.next
                return
            temp = temp.next
        print('No value : ', data)
        
    # To print elements of LL
    def display(self):
        if self.head is None:
            print('No elements in the linked list.')
            return
        
        # Traversing
        temp = self.head
        llstr = ''
        while temp:
            llstr += str(temp.data)
            temp = temp.next
            llstr += '-->' if temp is not None else ''
        print(llstr)
        return
    
    # To remove continuous duplicates
    def remove_duplicate(self):
        if self.head is None:
            print('Empty LL')
            return
        current = self.head
        while current:
            after = current.next
            if after and after.data == current.data:
                while after and after.data == current.data:
                    after = after.next
                current.next = after.next
            current = current.next
        return
        
ll = LinkedList()
# ll.insert_at_beginning(5)
# ll.insert_at_beginning(10)

# ll.insert_at_end(20)
# ll.insert_at_end(30)

# ll.insert_values(['Luffy','Zoro','Sanji'])

# ll.get_length()

# ll.display()
# ll.insert_at('nami',4)

# ll.display()
# ll.remove_at(0)
# ll.display()
# ll.remove_at(4)
# ll.get_length()

# ll.insert_after_value('Naruto','nami')

# ll.remove_value('Luffy')
# ll.remove_value('Zoro')
# ll.remove_value('Sanji')

ll.insert_values([6,10,5,5,5,8,8,9])
ll.display()
ll.remove_duplicate()

ll.display()