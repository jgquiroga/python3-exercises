class Node:
    def __init__(self):
        self.value = None
        self.leftNode = None
        self.rigthNode = None

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def setRigth(self, rigth):
        self.rigthNode = rigth

    def getRigth(self):
        return self.rigthNode

    def setLeft(self, left):
        self.leftNode = left

    def getLeft(self):
        return self.leftNode

    def printAsLinkedList(self):
        print (self.value)
        if self.rigthNode is not None:
            self.rigthNode.printAsLinkedList()

    #
    # Exercise taken from:
    # Flatten a binary tree into linked list
    # https://www.geeksforgeeks.org/flatten-a-binary-tree-into-linked-list/
    #
    # Explanation:
    # The flatten method is used recursively to create a linked list in place.
    # Returns the last node so we can use it in a high order Node
    # 
    def flatten(self):
        if self is None:
            return None

        left = self.getLeft()
        rigth = self.getRigth()

        lastNode = self
        if left is not None:
            lastNode = left.flatten()

            # Last Node replaces the right node
            lastNode.setRigth(rigth)
            self.setRigth(left)

        self.setLeft(None)

        if rigth is not None:
            lastNode = rigth.flatten()

        return lastNode

def example1():
    node6 = Node()
    node6.setValue(6)
    node5 = Node()
    node5.setValue(5)
    node5.setRigth(node6)
    node3 = Node()
    node3.setValue(3)
    node4 = Node()
    node4.setValue(4)
    node2 = Node()
    node2.setValue(2)
    node2.setLeft(node3)
    node2.setRigth(node4)
    node1 = Node()
    node1.setValue(1)
    node1.setLeft(node2)
    node1.setRigth(node5)
    binaryTree = node1

    return binaryTree


def main():
    binaryTree = example1()

    print('* right branch without flatten:')

    binaryTree.printAsLinkedList()

    binaryTree.flatten()

    print('* right branch flatten:')

    binaryTree.printAsLinkedList()

if __name__ == "__main__":
    main()