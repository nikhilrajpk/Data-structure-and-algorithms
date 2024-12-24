class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self,data):
        if data == self.data:
            return
        # lesser data
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    def search(self,val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def inOrder_traversal(self):
        elements = []
        # taking left data
        if self.left:
            elements += self.left.inOrder_traversal()
        #taking the node data
        elements.append(self.data)
        # taking the right data
        if self.right :
            elements += self.right.inOrder_traversal()
        
        return elements
    def preOrder_traversal(self):
        elements = []
        # taking node data
        elements.append(self.data)
        # taking left data
        if self.left:
            elements += self.left.preOrder_traversal()
        # taking right data
        if self.right:
            elements += self.right.preOrder_traversal()
        
        return elements
    def postOrder_traversal(self):
        elements = []
        # taking left data
        if self.left:
            elements += self.left.postOrder_traversal()
        # taking right data
        if self.right:
            elements += self.right.postOrder_traversal()
        # taking node data
        elements.append(self.data)
        
        return elements
    
    def find_min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()
    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()
    def total_sum(self,total=0):
        if self.left:
            total = self.left.total_sum(total)         
        total += self.data
        if self.right:
            total = self.right.total_sum(total)
        return total
        
    def delete_node(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_node(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_node(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_val = self.right.find_min()
            self.data = min_val
            
            self.right = self.right.delete_node(min_val)
            
        return self

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,18,34]
    numbers_tree = build_tree(numbers)
    # print(numbers_tree.search(2))
    # print('inOrder:',numbers_tree.inOrder_traversal())
    # print('preOrder:',numbers_tree.preOrder_traversal())
    # print('postOrder:',numbers_tree.postOrder_traversal())
    # print('minimum value from the tree : ',numbers_tree.find_min())
    # print('maximum value from the tree : ',numbers_tree.find_max())
    # print('total sum of the tree : ',numbers_tree.total_sum())
    # numbers_tree.delete_node(32)
    # print('inOrder:',numbers_tree.inOrder_traversal())

    
    # countries = ['India','China','Germany','UK','USA','Japan','Italy']
    # countries_tree = build_tree(countries)
    # print('India exist in the tree ? :',countries_tree.search('India'))
    # print('Sweden exist in the tree ? :',countries_tree.search('Sweden'))
    # print('inOrder:',countries_tree.inOrder_traversal())