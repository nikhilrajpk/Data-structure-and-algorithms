class TreeNode:
    def __init__(self,name,designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    def print_tree(self,arg):
        space = '   ' * self.get_level()
        prefix = space + '|__' if self.parent else ''
        if arg == 'both':
            print(prefix + self.name, '(',self.designation,')')
        elif arg == 'name':
            print(prefix+self.name)
        else:
            print(prefix+self.designation)
        if self.children:
            for child in self.children:
                child.print_tree(arg)

def bulid_office_tree():
    root = TreeNode('Nilpul','CEO')
    
    cto = TreeNode('Chinmay','CTO')
    infra_head = TreeNode('Vishwa','Infrastructure Head')
    infra_head.add_child(TreeNode('Dhaval','Cloud Manager'))
    infra_head.add_child(TreeNode('Abhijith','App Manager'))
    
    app_head = TreeNode('Aamir','Application Head')
    
    hr_head = TreeNode('Gels','HR Head')
    hr_head.add_child(TreeNode('Peter','Recruitment Manager'))
    hr_head.add_child(TreeNode('Waqas','Policy Manager'))
    
    root.add_child(cto)
    root.add_child(hr_head)
    cto.add_child(infra_head)
    cto.add_child(app_head)
    
    return root

if __name__ == '__main__':
    root = bulid_office_tree()
    root.print_tree('both')
    print('________________________________')
    root.print_tree('name')
    print('________________________________')
    root.print_tree('designation')
    print('________________________________')
    pass