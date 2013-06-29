class Empty(Exception):
    pass


class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class Stack(object):
    def __init__(self):
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size

    def empty(self):
        return self.top is None

    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.empty():
            raise Empty()
        item = self.top.item
        self.top = self.top.next
        self.size -= 1
        return item


def main():
    n = 10
    st = Stack()
    assert st.empty()

    expected = range(n)
    for i, x in enumerate(expected):
        assert len(st) == i
        st.push(x)
        assert len(st) == i + 1
    expected.reverse()

    actual = []
    while not st.empty():
        actual.append(st.pop())
    assert actual == expected
    assert len(st) == 0

    print('All tests passed')


if __name__ == '__main__':
    main()
