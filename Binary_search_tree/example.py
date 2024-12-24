class Binary:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self,data):
        if data == self.data:
            return 
        if data < self.data:
            if self.left :
                self.left.add_child(data)
            else:
                self.left = Binary(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Binary(data)
                
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data
        
    def remove(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.remove(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.remove(val)
        else:
            if not self.left and not self.right:
                return None
            if not self.left:
                return self.right
            if not self.right:
                return self.left
            min_val = self.find_min()
            self.data = min_val
            self.right = self.right.remove(min_val)
        return self
    
    