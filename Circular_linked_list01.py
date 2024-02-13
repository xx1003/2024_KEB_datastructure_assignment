import random
import math


class Node:
    def __init__(self):
        self.data = None
        self.link = None


head, tail, pre, current = None, None, None, None


def make_store():
    store_name = 65
    for i in range(10):
        insert_store((chr(store_name), random.randint(1, 100), random.randint(1, 100)))
        store_name += 1


def distance(node):
    return math.sqrt(pow(node.data[1], 2) + pow(node.data[2], 2))


def insert_store(store_data):
    global head, tail, pre, current
    new_node = Node()
    new_node.data = store_data

    if head is None:
        head = new_node
        tail = new_node
        head.link = tail
        tail.link = head
        return
    elif distance(new_node) < distance(head):
        new_node.link = head
        tail.link = new_node
        head = new_node
        return
    else:
        current = head
        while current.link != head:
            pre = current
            current = current.link
            if distance(new_node) < distance(current):
                new_node.link = current
                pre.link = new_node
                return
        current.link = new_node
        new_node.link = head
        tail = new_node


def print_nodes():
    global head
    current = head
    while True:
        print(f"{current.data[0]} 편의점, 거리: {distance(current)}")
        current = current.link
        if current == head:
            break


make_store()
print_nodes()