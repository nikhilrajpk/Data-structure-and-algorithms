class TreeNode:
    def __init__(self,location):
        self.location = location
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
    def print_tree(self,level):
        space = '   ' * self.get_level()
        prefix = space + '|__' if self.parent else ''
        print(prefix + self.location)
        if self.get_level() < level:
            if self.children:
                for child in self.children:
                    child.print_tree(level)
def build_location_tree():
    root = TreeNode('Global')
    
    india = TreeNode('India')
    
    gujarat = TreeNode('Gujarat')
    gujarat.add_child(TreeNode('Ahmedabad'))
    gujarat.add_child(TreeNode('Baroda'))
    
    karnataka = TreeNode('Karnataka')
    karnataka.add_child(TreeNode('Bengaluru'))
    karnataka.add_child(TreeNode('Mysore'))
    
    india.add_child(gujarat)
    india.add_child(karnataka)
    
    usa = TreeNode('USA')
    
    newJearsy = TreeNode('New Jearsy')
    newJearsy.add_child(TreeNode('Princeton'))
    newJearsy.add_child(TreeNode('Trenton'))
    
    california = TreeNode('California')
    california.add_child(TreeNode('San Fransisco'))
    california.add_child(TreeNode('Mountain View'))
    california.add_child(TreeNode('Palo Alto'))
    
    usa.add_child(newJearsy)
    usa.add_child(california)
    
    root.add_child(india)
    root.add_child(usa)
    
    return root

if __name__ == '__main__':
    root = build_location_tree()
    root.print_tree(3)
    pass