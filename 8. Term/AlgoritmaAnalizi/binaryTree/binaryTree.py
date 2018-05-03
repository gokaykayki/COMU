import random


class Node:
    def __init__(self, data, depth = 0):

        self.left = None
        self.right = None
        self.data = data
        self.depth = depth

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data, self.depth + 1)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data, self.depth + 1)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def getDepths(self, sums):
        if self.left:
            self.left.getDepths(sums)
        sums.append(self.depth)
        if self.right:
            self.right.getDepths(sums)


def fillBinaryTree(root, size, value):
    for i in range(size - 1):
        root.insert(random.randint(0, value))


def getSumsOfDepths(root):
    sums = []
    root.getDepths(sums)
    result = 0
    for i in sums:
        result += i
    return result

size_of_binary_tree = int(input("Enter size of binary tree: "))
max_value_limit_of_tree = int(input("Enter max value limit of tree: "))

root = Node(random.randint(0, max_value_limit_of_tree))

fillBinaryTree(root, size_of_binary_tree, max_value_limit_of_tree)

print("Printing Tree:"), root.printTree()
print("Sums of Depths: ", getSumsOfDepths(root))
