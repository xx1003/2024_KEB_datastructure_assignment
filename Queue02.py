def is_full():
    global size, queue, front, rear
    if ((rear+1)%size) == front:
        return True
    return False


def is_empty():
    global size, queue, front, rear
    if front == rear:
        return True
    return False


def enqueue(data):
    global size, queue, front, rear, time
    if is_full():
        return
    rear = (rear+1)%size
    queue[rear] = data
    time += data[1]


def dequeue():
    global size, queue, front, rear, time
    if is_empty():
        return
    front = (front+1)%size
    data = queue[front]
    queue[front] = None
    time -= data[1]


def peek():
    global size, queue, front, rear
    if is_empty():
        return
    return queue[(front+1)%size]


def print_time():
    global size, queue, front, rear, time
    if is_full():
        print(f"최종 대기 콜 --> {queue}")
        print("프로그램 종료!")
        return
    print(f"귀하의 대기 예상시간은 {time} 분입니다.")
    print(f"현재 대기 콜 --> {queue}")
    print()


size = 6
queue = [None for i in range(6)]
front = rear = 0
time = 0

if __name__ == "__main__":
    print_time()

    enqueue(('사용', 9))
    print_time()

    enqueue(('고장', 3))
    print_time()

    enqueue(('환불', 4))
    print_time()

    enqueue(('환불', 4))
    print_time()

    enqueue(('고장', 3))
    print_time()