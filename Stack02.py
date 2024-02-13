stack = [None for i in range(100)]
top = -1
size = 100


def push(data):
    global stack, top
    top += 1
    stack[top] = data


def pop():
    global stack, top
    temp = stack[top]
    stack[top] = None
    top -= 1
    return temp


f = open('진달래꽃.txt', 'r')
poem = f.read()
for c in poem:
    push(c)
f.close()

nf = open('reverse_진달래꽃.txt', 'w')
while top != -1:
    nf.write(pop())
nf.close()
