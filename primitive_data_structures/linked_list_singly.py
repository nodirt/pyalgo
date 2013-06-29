class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = None


class SinglyLinkedList(object):
    def __init__(self):
        self.head = Node()
        self.tail = None
        self.count = 0

    def __len__(self):
        return self.count

    def __getitem__(self, index):
        return self._prev_for(index).next.value

    def __setitem__(self, index, value):
        self._prev_for(index).next.value = value

    def nodes(self):
        node = self.head.next
        while node:
            yield node
            node = node.next

    def __iter__(self):
        for node in self.nodes():
            yield node.value

    def is_empty(self):
        return self.count == 0

    def append(self, value):
        node = Node(value)
        if self.tail is None:
            self.head.next = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.count += 1
        return node

    def _prev_for(self, index):
        node = self.head
        for i in xrange(index):
            node = node.next
            if node is None:
                raise IndexError('Invalid index: %d' % index)
        assert node and node.next
        return node

    def pop(self, index):
        prev = self._prev_for(index)
        value = prev.next.value
        prev.next.value = None
        prev.next = prev.next.next
        self.count -= 1
        return value

    def insert(seft, after, value):
        if after is None:
            after = self.head
        after.next = Node(value, after.next)
        self.count += 1
        return after.next


def main():
    n = 100
    lst = SinglyLinkedList()
    for i in range(n):
        assert len(lst) == i
        lst.append(i)
        assert len(lst) == i + 1

    assert list(lst) == range(n)
    print('All tests passed')


if __name__ == '__main__':
    main()
