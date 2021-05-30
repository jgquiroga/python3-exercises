class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.rigth = None

    #
    # Returns a list of items to traverse in a recursively way
    #
    def traverse(self):

        # list of nodes of the current branch
        nodes = [self]
        
        if self.left is not None:
            nodes.extend(self.left.traverse())

        if self.rigth is not None:
            nodes.extend(self.rigth.traverse())
        
        return nodes

#
# Exercise taken from:
# Level Order Binary Tree Traversal
# https://www.geeksforgeeks.org/level-order-tree-traversal/
#
# Explanation:
# Prints recursively the values of the binary tree
# 
def printNodes(nodes):
    for node in nodes:
        print(node.value)

    

def example1():
    node6 = Node(6)
    node5 = Node(5)
    node5.rigth = node6
    node3 = Node(3)
    node4 = Node(4)
    node2 = Node(2)
    node2.left = node3
    node2.rigth = node4
    node1 = Node(1)
    node1.left = node2
    node1.rigth = node5
    binaryTree = node1

    return binaryTree


def main():
    binaryTree = example1()

    printNodes(binaryTree.traverse())

if __name__ == "__main__":
    main()