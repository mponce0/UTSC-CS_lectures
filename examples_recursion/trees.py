####################################################################
# @Title: Example of trees definitions using recursuve classes
# @Author: Marcelo Ponce
# @Date: March 2021
####################################################################

# binary tree
class bTree:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

# example
root = bTree()
root.data = "root"
root.left = bTree()
root.left.data = "left"
root.right = bTree()
root.right.data = "right"

print(root)


#######################################################


# arbitrary childs
class aTree:
    def __init__(self, data):
        self.children = []
        self.data = data

# example
left = aTree("left")
middle = aTree("middle")
right = aTree("right")
root = aTree("root")
root.children = [left, middle, right]

print(root)


######################################################

class Tree(object):
    "Generic tree node."
    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

# Example
#    *
#   /|\
#  1 2 +
#     / \
#    3   4
t = Tree('*', [Tree('1'),
               Tree('2'),
               Tree('+', [Tree('3'),
                          Tree('4')])])

print(t)


######################################################

# tree using dictionaries
tree = {
   "a": ["b", "c"],
   "b": ["d", "e"],
   "c": [None, "f"],
   "d": [None, None],
   "e": [None, None],
   "f": [None, None],
}

print(tree)


######################################################
