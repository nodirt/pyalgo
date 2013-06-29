class Error(Exception):
    pass


class FixedSizeQueue(object):
    def __init__(self, max_size=100):
        self.items = [None] * (max_size + 1)
        self.head = 0
        self.tail = 0

    def __len__(self):
        size = self.tail - self.head
        if size < 0:
            size = len(self.items) - size
        return size

    def _inc(self, x):
        x += 1
        if x >= len(self.items):
            x -= len(self.items)
        return x

    def empty(self):
        return self.head == self.tail

    def full(self):
        return self._inc(self.tail) == self.head

    def enqueue(self, item):
        if self.full():
            raise Error('Queue is full: %s' % len(self.items))
        self.items[self.tail] = item
        self.tail = self._inc(self.tail)

    def dequeue(self):
        if self.empty():
            raise Error('Queue is empty')
        item = self.items[self.head]
        self.items[self.head] = None
        self.head = self._inc(self.head)
        return item


def main():
    n = 10
    q = FixedSizeQueue(max_size=n)
    assert q.empty()

    expected = range(n)
    for i, x in enumerate(expected):
        assertlen(q) == i
        q.enqueue(x)
        assertlen(q) == i + 1
    assert q.full()

    actual = []
    while not q.empty():
        actual.append(q.dequeue())
    assert actual == expected
    print('All tests passed')


if __name__ == '__main__':
    main()
