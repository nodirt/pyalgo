class Empty(Exception):
    pass


class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def empty(self):
        return self.head is None

    def enqueue(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        if self.empty():
            raise Empty()
        item = self.head.item
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1
        return item


def main():
    n = 10
    q = Queue()
    assert q.empty()

    expected = range(n)
    for i, x in enumerate(expected):
        assert len(q) == i
        q.enqueue(x)
        assert len(q) == i + 1

    actual = []
    while not q.empty():
        actual.append(q.dequeue())
    assert actual == expected
    assert len(q) == 0

    print('All tests passed')


if __name__ == '__main__':
    main()
