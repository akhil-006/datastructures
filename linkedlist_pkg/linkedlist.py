class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, node):
        if not node:
            raise ValueError('Invalid node!')

        if not self.head:
            self.head = node
        else:
            curr = self.head
            prev = None
            while curr:
                prev = curr
                curr = prev.next
            prev.next = node

    def delete_last_node(self):
        curr = self.head
        if not curr:
            raise ValueError('Linked list is empty!')

        if curr.next is None:
            self.head = None
            return

        prev = None
        while curr and curr.next:
            prev = curr
            curr = prev.next

        if prev:
            prev.next = None

    def insert_node_after(self, pos, node):
        if not node:
            raise TypeError('Node cannot be empty!')

        node_index = 0
        if node_index == pos:
            node.next = self.head
            self.head = node
            return

        node_index += 1
        curr = self.head
        while node_index != pos:
            prev = curr
            curr = prev.next
            node_index += 1
        else:
            prev = curr

        if not prev:
            raise IndexError(f'Index(position={pos}) out of bounds error!')

        node.next = prev.next
        prev.next = node

    def delete_node_after(self, pos):
        node_idx = 0
        curr = self.head
        if not curr:
            raise TypeError('Delete Failed: Linked list is empty!')

        if node_idx == pos:
            curr = curr.next
            self.head = curr
            return

        prev = curr
        while node_idx != pos:
            prev = curr
            if not (prev and prev.next):
                raise IndexError(f'Index(position={pos}) out of bounds error!')
            curr = prev.next
            node_idx += 1

        prev.next = curr.next

    def search_linkedlist(self, data):
        node_idx = 0
        curr = self.head
        if not curr:
            print('Linked list is empty!')
            return

        while curr.data != data:
            curr = curr.next
            node_idx += 1
            if not curr:
                node_idx = -1
                break

        return node_idx

    def print_nodes(self):
        curr = self.head
        if not curr:
            print('Linked list is empty!!')
            return
        i = 0
        while curr is not None:
            print(f'node{i}: ', curr.data)
            curr = curr.next
            i += 1


if __name__ == '__main__':
    print('# =======================Inserting some nodes=======================')
    node0 = Node(int(input()))
    node1 = Node(int(input()))
    node2 = Node(int(input()))
    node3 = Node(int(input()))
    objll = LinkedList()
    objll.insert_node(node0)
    objll.insert_node(node1)
    objll.insert_node(node2)
    objll.insert_node(node3)
    print('# =======================Printing the inserted nodes=======================')
    objll.print_nodes()
    print('# =======================Deleting the last node=======================')
    objll.delete_last_node()
    print('# =======================After deletion of last node=======================')
    objll.print_nodes()
    print('# =======================Insert node at position=======================')
    pos = int(input())
    node5 = Node(int(input()))
    objll.insert_node_after(pos, node5)
    print(f'# =======================After inserting node at position={pos}, the linked-list is=======================')
    objll.print_nodes()
    pos = int(input())
    print(f'# =======================Deleting node at position={pos}, the linked-list is=======================')
    objll.delete_node_after(pos)
    objll.print_nodes()
    print(f'# =======================Searching a node with data, the index of that node is=======================')
    index = objll.search_linkedlist(int(input()))
    print('index ', 'FOUND: ' + str(index) if index >= 0 else 'NOT FOUND!')


