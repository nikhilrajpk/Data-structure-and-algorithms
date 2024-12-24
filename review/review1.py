# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)

# print(fact(4))

# def binary(nums,target):
#     start = 0
#     end = len(nums)-1
#     while start <= end:
#         mid = start + ((end-start)//2)
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] > target:
#             end = mid-1
#         else:
#             start = mid+1
#     return -1

# nums = [3, 1, 4, 5, 9, 2, 6]
# nums.sort()
# print(nums)
# target = 4
# print(binary(nums,target))


class Node:
    def __init__(self,data,next):
        self.data = data
        self.next  = next
class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.head = node
        return
    def insert_at_end(self,data):
        node = Node(data,None)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        return
    def display(self):
        if self.head is None:
            print('empty')
            return 
        temp = self.head
        llstr = []
        while temp:
            llstr.append(str(temp.data))
            temp = temp.next
            if temp: llstr.append('-->')
        print(''.join(llstr))
        return
    
ll = SLinkedList()
ll.insert_at_beginning(1)
ll.insert_at_end(2)
ll.display()