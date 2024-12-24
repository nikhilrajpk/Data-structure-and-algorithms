class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    def get_level(self):
        level = 0
        p = self.parent
        while p :
            level += 1
            p = p.parent
        return level
    def display(self):
        space = '   '* self.get_level()
        prefix = space + '|__' if self.parent else ''
        print(prefix + self.data)
        if self.children :
            for child in self.children:
                child.display()
    def contains(self,val):
        if val == self.data:
            return True
        if self.children:
            for child in self.children:
                if child.contains(val):
                    return True
        else:
            return False

def build_tree():
    root = TreeNode('Electronics')
    
    mobile = TreeNode('Mobile')
    mobile.add_child(TreeNode('IOS'))
    mobile.add_child(TreeNode('Android'))
    
    tv = TreeNode('TV')
    tv.add_child(TreeNode('LED'))
    tv.add_child(TreeNode('LCD'))
    
    root.add_child(mobile)
    root.add_child(tv)
    
    return root

if __name__== '__main__':
    root = build_tree()
    root.display()
    print(root.contains('TV'))