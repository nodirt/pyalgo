"""AVL tree, a balanced binary search tree

Invariant:
    For every node in the tree, the absolute difference between heights
    of child nodes is at most 1. If a child is absent its height is -1.

Properties:
    Search: O(log(n))
    Insert: O(log(n))
    Delete: O(log(n))
    Space: O(n)

Description:
    Wikipedia: http://en.wikipedia.org/wiki/AVL_tree
    Cormen [1]: problems for Chapter 13, page 333

History:
    Authors: Georgy Adelson-Velskii and Evgeniy Landis (1962),
    two Soviet matematicians.
"""
import math

class AvlNode(object):
    def __init__(self, key, height=0):
        self.key = key
        self.left = None
        self.right = None
        self.height = height

    def __getitem__(self, right):
        return self.right if right else self.left

    def __setitem__(self, right, node):
        if right:
            self.right = node
        else:
            self.left = node

    def children_height(self):
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1
        return (left_height, right_height)

    def update_height(self):
        self.height = max(self.children_height()) + 1

    def is_balanced(self, recurse=False):
        left_height, right_height = self.children_height()
        if abs(left_height - right_height) > 1:
            return False

        if recurse:
            if self.left and not self.left.is_balanced():
                return False
            if self.right and not self.right.is_balanced():
                return False

        return True

    def rotate(self, right):
        left = not right
        other = self[left]
        assert(other)
        self[left] = other[right]
        other[right] = self
        self.update_height()
        other.update_height()
        return other

    def fix_balance(self):
        self.update_height()
        if self.is_balanced():
            return self

        left_height, right_height = self.children_height()
        right = left_height > right_height
        left = not right
        other = self[left]
        assert(other)
        
        if not other[left]:
            other = other.rotate(left)
            self[left] = other
        result = self.rotate(right)
        assert(result == other)
        assert(other.is_balanced() and self.is_balanced())
        return result


    def insert(self, key):
        if self.key == key:
            raise KeyError('Duplicate key')

        go_right = key > self.key
        if self[go_right]:
            self[go_right] = self[go_right].insert(key)
        else:
            self[go_right] = AvlNode(key)

        return self.fix_balance()

    def extract_leftmost(self):
        if not self.left:
            return (self, self.right)

        result, new_child = self.left.extract_leftmost()
        self.left = new_child
        return (result, self.fix_balance())

    def delete(self, key):
        if self.key != key:
            right = key > self.key
            self[right] = self[right].delete(key)
            result = self
        else:
            if not self.right:
                return self.left

            result, new_child = self.right.extract_leftmost()
            result.left = self.left
            result.right = new_child

        return result.fix_balance()

    def in_order(self, fn):
        if self.left:
            self.left.in_order(fn)
        fn(self)
        if self.right:
            self.right.in_order(fn)


class AvlTree(object):
    def __init__(self):
        self.root = None
        self.count = 0

    def __len__(self):
        return self.count

    def search(self, key):
        """O(log(n))"""
        node = self.root
        while node:
            if node.key == key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right

        return None

    def __contains__(self, key):
        return self.search(key) is not None

    def insert(self, key):
        if self.root:
            self.root = self.root.insert(key)
        else:
            self.root = AvlNode(key)
        self.count += 1

    def __delitem__(self, key):
        if self.root is None:
            raise KeyError('Key not found')
        self.root.delete(key)
        self.count -= 1

    def in_order(self, fn):
        if self.root:
            self.root.in_order(fn)

    def is_balanced(self):
        return not self.root or self.root.is_balanced(recurse=True)

    def height(self):
        return self.root.height if self.root else 0


def main():
    tree = AvlTree()

    def test_height():
        expected_height = math.log(len(tree), 2)
        assert(abs(expected_height - tree.height()) < 2)

    for x in xrange(100):
        tree.insert(x)
        assert(tree.is_balanced())

    test_height()

    for x in xrange(1, 100, 9):
        del tree[x]
        assert(tree.is_balanced())

    test_height()

    ordered = []
    tree.in_order(lambda n: ordered.append(n.key))
    assert(ordered == list(sorted(ordered)))
    


    print('All tests passed')


if __name__ == '__main__':
    main()