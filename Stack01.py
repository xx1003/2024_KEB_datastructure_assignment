stack = [None for i in range(6)]
top = -1
size = 6


def is_full():
    if top == size - 1:
        return True
    return False


def is_empty():
    if top == -1:
        return True
    return False


def push(stone):
    global stack, top

    if is_full():
        pass
    else:
        top += 1
        stack[top] = stone


def pop():
    global stack, top

    if is_empty():
        pass
    else:
        temp = stack[top]
        stack[top] = None
        top -= 1
        return temp


for i in range(6):
    color = input()
    push(color)


def way_to_cookie():
    print("과자집에 가는길 : ", end='')
    for i in stack:
        print(f"{i} --> ", end='')
    print("과자집")


def way_to_home():
    print("우리집에 오는길 : ", end='')
    while not is_empty():
        print(f"{pop()} --> ", end='')
    print("우리집")


way_to_cookie()
way_to_home()