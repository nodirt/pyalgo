class Error(Exception):
    pass


class FixedSizeStack(object):
    def __init__(self, max_size=100):
        self.items = [None] * max_size
        self.size = 0

    def __len__(self):
        return self.size

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == len(self.items)

    def enqueue(self, item):
        if self.full():
            raise Error('Queue is full: %s' % len(self.items))
        self.items[self.size] = item
        self.size += 1

    def dequeue(self):
        if self.empty():
            raise Error('Queue is empty')
        self.size -= 1
        item = self.items[self.size]
        self.items[self.size] = None
        return item


def main():
    n = 10
    st = FixedSizeStack(max_size=n)
    assert st.empty()
    expected = range(n)
    for i, x in enumerate(expected):
        assert len(st) == i
        st.enqueue(x)
        assert len(st) == i + 1
    assert st.full()
    expected.reverse()
    actual = []
    while not st.empty():
        actual.append(st.dequeue())
    assert actual == expected

    print('All tests passed')


if __name__ == '__main__':
    main()
