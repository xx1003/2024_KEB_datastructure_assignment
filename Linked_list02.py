import random


class Node:
    def __init__(self):
        self.data = None
        self.link = None


head, pre, current = None, None, None


def insert_number(num):
    global head, pre, current
    new_node = Node()
    new_node.data = num

    if head is None:
        head = new_node
        return
    elif new_node.data < head.data:
        new_node.link = head
        head = new_node
        return
    else:
        current = head
        while current.link is not None:
            pre = current
            current = current.link
            if new_node.data < current.data:
                new_node.link = current
                pre.link = new_node
                return
        current.link = new_node


def lotto():
    for i in range(6):
        insert_number(random.randint(1, 45))


def print_nodes():
    global head
    current = head
    while current is not None:
        print(current.data, end=' ')
        current = current.link


if __name__ == "__main__":
    lotto()
    print_nodes()
