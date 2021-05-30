class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.rigth = None

    def printAsLinkedList(self):
        print (self.value)
        if self.rigth is not None:
            self.rigth.printAsLinkedList()

#
# Exercise taken from:
# Flatten a binary tree into linked list
# https://www.geeksforgeeks.org/flatten-a-binary-tree-into-linked-list/
#
# Explanation:
# The flatten method is used recursively to create a linked list in place.
# Returns the last node so we can use it in a high order Node
# 
def flatten(node):
    if node is None:
        return None

    left = node.left
    rigth = node.rigth

    lastNode = node
    if left is not None:
        lastNode = flatten(left)

        # Last Node replaces the right node
        lastNode.rigth = rigth
        node.rigth = left

    node.left = None

    if rigth is not None:
        lastNode = flatten(rigth)

    return lastNode

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
    node1.rigth =node5
    binaryTree = node1

    return binaryTree


def main():
    binaryTree = example1()

    print('* right branch without flatten:')

    binaryTree.printAsLinkedList()

    flatten(binaryTree)

    print('* right branch flatten:')

    binaryTree.printAsLinkedList()

if __name__ == "__main__":
    main()