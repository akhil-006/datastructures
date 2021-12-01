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
                # no harm in setting left = node but you can do it directly thereby decreasing time complexity
                # left = node
                # root.left = left
                root.left = node
            else:
                while left and node.data <= left.data:
                    if not left.left:
                        left.left = node
                        return
                    else:
                        left = left.left

                right = left.right
                if not right:
                    left.right = node
                else:
                    while right and node.data > right.data:
                        if not right.right:
                            right.right = node
                            return
                        else:
                            right = right.right

                    left = right.left
                    if not left:
                        right.left = node
                    else:
                        left.right = node
        else:
            right = root.right
            if not right:
                root.right = node
            else:
                while right and node.data > right.data:
                    if not right.right:
                        right.right = node
                        return
                    else:
                        right = right.right

                left = right.left
                if not left:
                    right.left = node
                else:
                    while left and node.data <= left.data:
                        if not left.left:
                            left.left = node
                            return
                        else:
                            left = left.left

                    right = left.right
                    if not right:
                        left.right = node
                    else:
                        left.left = node

    def print_nodes(self):
        if not self.node:
            raise ValueError(f'{BinaryTree.__name__} is empty!')
        left = self.node.left
        while left:
            print(left.data)
            right = left.right
            left = left.left
            if right:
                print(right.data)
        print(self.node.data)
        right = self.node.right
        while right:
            print(right.data)
            left = right.left
            right = right.right
            if left:
                print(left.data)


if __name__ == '__main__':
    root = Node(100)
    node1 = Node(60)
    node2 = Node(150)
    node3 = Node(60)
    node4 = Node(70)
    node5 = Node(50)
    node6 = Node(80)
    node7 = Node(6)
    node8 = Node(88)
    node9 = Node(188)
    node10 = Node(0)
    node11 = Node(152)
    node12 = Node(67)
    node13 = Node(68)
    node14 = Node(81)
    node15 = Node(-1)
    node16 = Node(155)
    node17 = Node(110)
    node18 = Node(105)
    node19 = Node(151)
    node20 = Node(106)
    node21 = Node(105)
    objBT = BinaryTree(root)
    objBT.insert(node1)
    objBT.insert(node2)
    objBT.insert(node3)
    objBT.insert(node4)
    objBT.insert(node5)
    objBT.insert(node6)
    objBT.insert(node7)
    objBT.insert(node8)
    objBT.insert(node9)
    objBT.insert(node10)
    objBT.insert(node11)
    objBT.insert(node12)
    objBT.insert(node13)
    objBT.insert(node14)
    objBT.insert(node15)
    objBT.insert(node16)
    objBT.insert(node17)
    objBT.insert(node18)
    objBT.insert(node19)
    objBT.insert(node20)
    objBT.insert(node21)
    objBT.print_nodes()

