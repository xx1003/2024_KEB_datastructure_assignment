class Node:
    def __init__(self):
        self.data = None
        self.prev = None
        self.next = None


head, tail, pre, current = None, None, None, None


node1 = Node()
node1.data = '다현'
head = node1

node2 = Node()
node2.data = '정연'
node2.prev = node1
node1.next = node2

node3 = Node()
node3.data = '쯔위'
node2.next = node3
node3.prev = node2

node4 = Node()
node4.data = '사나'
node3.next = node4
node4.prev = node3

node5 = Node()
node5.data = '지효'
node4.next = node5
node5.prev = node4

tail = node5


def print_nodes():
    global head
    current = head
    print("정방향--> ", end='')
    while current != None:
        print(current.data, end=" ")
        current = current.next
    print()


def reverse_nodes():
    global tail
    current = tail
    print("역방향--> ", end='')
    while current != None:
        print(current.data, end=" ")
        current = current.prev


print_nodes()
reverse_nodes()