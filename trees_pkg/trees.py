class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class BinaryTree:
    def __init__(self, root):
        if not isinstance(root, Node):
            raise TypeError(f'{root} node must be an instance of class Node')
        self.node = root

    def insert(self, node):
        """
        In binary tree the insertion follows the pattern that if the data in the node is less or equal to the data in
        the current-node then it will be paced to the left of the tree and if the data is greater than the current-node
        then it will placed on the right side of the current-node.
        """
        if not node:
            raise TypeError(f'{node} node must be an instance of class Node')

        root = self.node
        if node.data <= root.data:
            left = root.left
            if not left:
                # no harm in setting left = node but you can do it directly thereby descraesing time complexity
                # left = node
                # root.left = left
                root.left = node
            else:
                while left.left and node.data <= left.data:
                    left = left.left
                left.left = node

        if node.data > root.data:
            right = root.right
            if not right:
                # right = node
                # root.right = right
                root.right = node
            else:
                while right.right and node.data > right.data:
                    right = right.right
                right.right = node

    def print_nodes(self):
        if not self.node:
            raise ValueError(f'{BinaryTree.__name__} is empty!')
        left = self.node.left
        while left:
            print(left.data)
            left = left.left
        print(self.node.data)
        right = self.node.right
        while right:
            print(right.data)
            right = right.right


if __name__ == '__main__':
    root = Node(10)
    node1 = Node(9)
    node2 = Node(11)
    node3 = Node(7)
    node4 = Node(12)
    node5 = Node(12)
    objBT = BinaryTree(root)
    objBT.insert(node1)
    objBT.insert(node2)
    objBT.insert(node3)
    objBT.insert(node4)
    objBT.insert(node5)
    objBT.print_nodes()

