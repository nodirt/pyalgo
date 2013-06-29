class Node(object):
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __len__(self):
        return self.count

    def __getitem__(self, index):
        return self._node_at(index).value

    def __setitem__(self, index, value):
        self._node_at(index).value = value

    def nodes(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __iter__(self):
        for node in self.nodes():
            yield node.value

    def append(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.count += 1
        return node

    def _node_at(self, index):
        node = self.head
        i = 0
        while True:
            if node is None:
                raise IndexError('Invalid index: %d' % index)
            if i >= index:
                break
            node = node.next
            i += 1

        assert node
        return node

    def pop(self, index):
        return self.remove(self._node_at(index))

    def remove(self, node):
        if type(node) != Node:
            raise ValueError('node is not a Node')
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        self.count -= 1
        return node.data

    def insert(seft, before, value):
        node = Node(value, after)

        if before:
            if before.prev:
                before.prev.next = node
                node.prev = before.prev
            before.prev = node
            node.next = before
            if self.head == before:
                self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.count += 1
        return after.next


def main():
    n = 100
    lst = DoublyLinkedList()
    for i in range(n):
        assert len(lst) == i
        lst.append(i)
        assert len(lst) == i + 1

    assert list(lst) == range(n)
    print('All tests passed')


if __name__ == '__main__':
    main()
