from linked_list import Node, LinkedList


def split(linked_list: LinkedList):
    mid = linked_list.length() // 2
    mid_node = linked_list.node_at(mid - 1)

    left = linked_list
    right = LinkedList()
    right.head = mid_node.next_node
    mid_node.next_node = None
    return left, right


def merge(left: LinkedList, right: LinkedList):
    left_node = left.head
    right_node = right.head

    merged_list = LinkedList()
    # Add a fake header
    merged_list.add_node(0)

    current_node = merged_list.head

    while None != left_node and None != right_node:
        if left_node.data < right_node.data:
            current_node.next_node = left_node
            left_node = left_node.next_node
            # current_node.next_node = None
        else:
            current_node.next_node = right_node
            right_node = right_node.next_node
        current_node = current_node.next_node

    if None != left_node:
        current_node.next_node = left_node
    if None != right_node:
        current_node.next_node = right_node
    # Discard the fake header
    merged_list.head = merged_list.head.next_node
    return merged_list


def merge_sort_recursive(linked_list: LinkedList, recursive_depth=0):
    if linked_list.length() <= 1:
        return linked_list
    left, right = split(linked_list)
    left_sorted = merge_sort_recursive(left, recursive_depth + 1)
    right_sorted = merge_sort_recursive(right, recursive_depth + 1)
    return merge(left_sorted, right_sorted)


def verify_sorted(linked_list: LinkedList):
    current = linked_list.head
    while None != current:
        next_node = current.next_node
        if None == next_node:
            break
        if current.data > next_node.data:
            return False
        current = next_node
    return True


linked_list = LinkedList()
linked_list.add_node(6)
linked_list.add_node(3)
linked_list.add_node(8)
linked_list.add_node(4)
linked_list.add_node(9)
linked_list.add_node(0)
linked_list.add_node(7)
linked_list.add_node(5)
linked_list.add_node(2)
linked_list.add_node(1)
print(linked_list)
print(verify_sorted(linked_list))
sorted_linked_list = merge_sort_recursive(linked_list)
print(sorted_linked_list)
print(verify_sorted(sorted_linked_list))
