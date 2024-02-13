queue = ['정국', '뷔', '지민', '진', '슈가']
size = 5


def dequeue():
    global queue, size
    if size == 0:
        print("식당 영업 종료!")
    elif size == 1:
        print(f"{queue[0]} 님 식당에 들어감")
        queue[0] = None
    else:
        print(f"{queue[0]} 님 식당에 들어감")
        start = 1
        while start < size:
            queue[start - 1] = queue[start]
            queue[start] = None
            start += 1
    size -= 1


def print_queue():
    print(f"대기 줄 상태 : {queue}")


def line():
    global size, queue
    while size >= 0:
        print_queue()
        dequeue()


line()
