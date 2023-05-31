class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self) -> str:
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def node_at(self, position):
        current = self.head
        idx = 0
        while idx < position:
            if None == current:
                return None
            current = current.next_node
            idx += 1
        return current

    def length(self) -> int:
        current = self.head
        size = 0
        while None != current:
            size += 1
            current = current.next_node
        return size

    def __repr__(self) -> str:
        as_repr = []
        current = self.head
        while None != current:
            if self.head == current:
                as_repr.append('Head: ' + current.__repr__())
            elif current.next_node == None:
                as_repr.append('Tail: ' + current.__repr__())
            else:
                as_repr.append(current.__repr__())

            current = current.next_node

        return ', '.join(as_repr)


def test_linked_list():
    linked_list = LinkedList()
    linked_list.add_node(5)
    linked_list.add_node(7)
    linked_list.add_node(3)
    linked_list.add_node(2)
    linked_list.add_node(6)
    linked_list.add_node(9)
    print(linked_list)


if __name__ == '__main__':
    test_linked_list()
