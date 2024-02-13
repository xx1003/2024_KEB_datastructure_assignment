class Node:
    def __init__(self):
        self.data = None
        self.link = None


head, pre, current = None, None, None


def insert_data(user_data):
    global head, pre, current
    new_node = Node()
    new_node.data = user_data

    if head is None:
        head = new_node
        return
    elif new_node.data[1] < head.data[1]:
        new_node.link = head
        head = new_node
        return
    else:
        current = head
        while current.link is not None:
            pre = current
            current = current.link
            if new_node.data[1] < current.data[1]:
                new_node.link = current
                pre.link = new_node
                return

        current.link = new_node


def print_nodes(start):
    global head
    current = head
    while current is not None:
        print(current.data, end=' ')
        current = current.link


if __name__ == "__main__":
    while True:
        user_name = input("이름--> ")
        if user_name == '':
            break
        user_email = input("이메일--> ")
        user_data = [user_name, user_email]
        insert_data(user_data)
        print_nodes(head)
        print()