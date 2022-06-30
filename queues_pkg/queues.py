
from collections import deque


class QueuesClass:
    def __init__(self):
        self._elements = deque()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

    def __iter__(self):
        while len(self._elements) > 0:
            yield self.dequeue()

    def __len__(self):
        return len(self._elements)


if __name__ == '__main__':
    queue = QueuesClass()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    for q in queue:
        # prints the stack elements in the oder of insertion i.e. FIFO
        print(q)
    
    print(len(queue))