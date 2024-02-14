class TreeNode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


sold = ['레쓰비캔커피', '레쓰비캔커피', '레쓰비캔커피', '도시락', '도시락',
        '삼각김밥', '레쓰비캔커피', '도시락', '코카콜라', '삼다수', '레쓰비캔커피',
        '레쓰비캔커피', '레쓰비캔커피', '츄파춥스', '츄파춥스', '레쓰비캔커피',
        '코카콜라', '츄파춥스', '삼각김밥', '코카콜라']


size = 0
root = None


def is_existed(data):
    current = root
    while current is not None:
        if data == current.data:
            return True
        elif data < current.data:
            current = current.left
        else:
            current = current.right
    return False


def insert_node(data):
    global size, root
    node = TreeNode()
    node.data = data

    if root is None:
        root = node
        size += 1
    else:
        current = root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = node
                    size += 1
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = node
                    size += 1
                    break
                else:
                    current = current.right


def preorder_print(node):
    if node is None:
        return
    print(node.data, end=' ')
    preorder_print(node.left)
    preorder_print(node.right)


for i in sold:
    if is_existed(i):
        continue
    else:
        insert_node(i)

print(f"오늘 판매된 물건(중복O) --> {sold}")
print()
print("이진 탐색 트리 구현 완료!")
print()
print("오늘 판매된 종류(중복X) -->", end=' ')
preorder_print(root)
