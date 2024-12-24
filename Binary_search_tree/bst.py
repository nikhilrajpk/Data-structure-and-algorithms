class BianrySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self,val):
        if val == self.data:
            return
        if val < self.data:
            if self.left:
                self.left.add_child(val)
            else:
                self.left = BianrySearchTreeNode(val)
        else:
            if self.right:
                self.right.add_child(val)
            else:
                self.right = BianrySearchTreeNode(val)
                
    def search(self,val):
        if val == self.data:
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
    
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
            
        return elements
    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
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
    def total_sum(self):
        total = 0
        if self.left:
            total += self.left.total_sum()
        total += self.data
        if self.right:
            total += self.right.total_sum()
        return total
    
    # def delete_node(self,val):
    #     if val < self.data:
    #         if self.left:
    #             self.left = self.left.delete_node(val)
    #     elif val > self.data:
    #         if self.right:
    #             self.right = self.right.delete_node(val)
    #     else:
    #         if self.left is None and self.right is None:
    #             return None
    #         if self.left is None:
    #             return self.right
    #         if self.right is None:
    #             return self.left
            
    #         min_val = self.right.find_min()         # Replacing with the minimum from right subtree.
    #         self.data = min_val
            
    #         self.right = self.right.delete_node(min_val)
    #     return self
        
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
            
            max_value = self.left.find_max()
            self.data = max_value
            
            self.left = self.left.delete_node(max_value)
        return self
    def closest(self,target):
        closest = self.data
        return self.closest_helper(target,closest)
    
    def closest_helper(self,target,closest):
        if self.data == target:
            return closest
        if abs(target - self.data) < abs(target - closest): closest = self.data
        if target < self.data:
            if self.left:
                return self.left.closest_helper(target,closest)
            else:
                return closest
        else:
            if self.right:
                return self.right.closest_helper(target,closest)
            else:
                return closest
            
def build_tree(elements):
    root = BianrySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,18,34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.search(3))
    print('in order traversal',numbers_tree.in_order_traversal())
    print('pre order traversal',numbers_tree.pre_order_traversal())
    print('post order traversal',numbers_tree.post_order_traversal())
    print('minimum from tree',numbers_tree.find_min())
    print('maximum from tree',numbers_tree.find_max())
    print('total sum : ',numbers_tree.total_sum())
    
    numbers_tree.delete_node(17)
    print('in order traversal',numbers_tree.in_order_traversal())
    
    target = 18
    print(f'closest value of {target} : ',numbers_tree.closest(target))