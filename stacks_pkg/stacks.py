from collections import deque


class StackClass:
    def __init__(self, *elem):
        self._elements = deque(elem)

    def push(self, elem):
        self._elements.append(elem)

    def pop(self):
        return self._elements.pop()

    def __iter__(self):
        while len(self._elements) > 0:
            yield self.pop()

    def __len__(self):
        return len(self._elements)


if __name__ == '__main__':
    stack = StackClass()
    stack.push("1")
    stack.push("4")
    stack.push("5")

    for s in stack:
        # prints the stack elements in reverse oder of insertion i.e. LIFO
        print(s)

    print(len(stack))

    # uncommenting the below line will yield an index-error as the stack is empty
    # stack.pop()
