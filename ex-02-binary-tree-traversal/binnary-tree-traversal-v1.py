class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.rigth = None

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def setRigth(self, rigth):
        self.rigth = rigth

    def getRigth(self):
        return self.rigth

    def setLeft(self, left):
        self.left = left

    def getLeft(self):
        return self.left


    #
    # Exercise taken from:
    # Level Order Binary Tree Traversal
    # https://www.geeksforgeeks.org/level-order-tree-traversal/
    #
    # Explanation:
    # Prints recursively the values of the binary tree
    # 
    def printBinaryTree(self):
        print (self.value)

        if self.left is not None:
            self.left.printBinaryTree()

        if self.rigth is not None:
            self.rigth.printBinaryTree()

def example1():
    node6 = Node(6)
    node5 = Node(5)
    node5.setRigth(node6)
    node3 = Node(3)
    node4 = Node(4)
    node2 = Node(2)
    node2.setLeft(node3)
    node2.setRigth(node4)
    node1 = Node(1)
    node1.setLeft(node2)
    node1.setRigth(node5)
    binaryTree = node1

    return binaryTree


def main():
    binaryTree = example1()

    binaryTree.printBinaryTree()

if __name__ == "__main__":
    main()