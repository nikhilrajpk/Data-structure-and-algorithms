class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    def add_child(self,child):
        child.parent = self                     # mac.parent = laptop
        self.children.append(child)             # laptop.children.append(mac)
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    def print_tree(self):
        space = ' ' * self.get_level() * 3
        prefix = space + '|__' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def bulid_product_tree():
    root = TreeNode('Electronics')
    
    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('Dell'))
    laptop.add_child(TreeNode('Samsung'))
    
    cellphone = TreeNode('Cellphone')
    cellphone.add_child(TreeNode('Iphone'))
    cellphone.add_child(TreeNode('Oneplus'))
    cellphone.add_child(TreeNode('Oppo'))
    
    tv = TreeNode('TV')
    tv.add_child(TreeNode('Impex'))
    tv.add_child(TreeNode('Toshiba'))
    tv.add_child(TreeNode('LG'))
    
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    
    return root

if __name__ == '__main__':
    root = bulid_product_tree()
    root.print_tree()
    pass