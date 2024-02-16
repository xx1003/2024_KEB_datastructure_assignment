graph = [
    [0, 80, 0, 10, 0, 0],
    [80, 0, 0, 40, 70, 0],
    [0, 0, 0, 0, 30, 60],
    [10, 40, 0, 0, 50, 0],
    [0, 70, 30, 50, 0, 20],
    [0, 0, 60, 0, 20, 0]
]
#           0       1   2       3       4      5
city = ['서울', '뉴욕', '런던', '북경', '방콕', '파리']

def print_graph(g):
    print('  ', end=' ')
    for v in range(len(city)):
        print(city[v], end=' ')
    print()
    for row in range(len(city)):
        print(city[row], end=' ')
        for col in range(len(city)):
            print(f"{graph[row][col]:2d}", end='  ')
        print()
    print()

print("## 해저 케이블 연결을 위한 전체 연결도 ##")
print_graph(graph)

arr = []
for i in range(len(city)):
    for j in range(len(city)):
        if graph[i][j] != 0:
            arr.append([graph[i][j], i, j])


arr.sort(key=lambda data: data[0])

new_arr = []
for i in range(0, len(arr), 2):
    new_arr.append(arr[i])


def is_existed(g, find):
    visited = []
    stack = []

    current = 0
    stack.append(current)
    visited.append(current)

    while len(stack) != 0:
        next = None
        for i in range(len(city)):
            if graph[current][i] != 0:
                if i in visited:
                    pass
                else:
                    next = i
                    break
        if next != None:
            current = next
            stack.append(current)
            visited.append(current)
        else:
            current = stack.pop()

    return find in visited


index = 0
while len(new_arr) > len(city) - 1:
    start = new_arr[index][1]
    end = new_arr[index][2]
    save_cost = new_arr[index][0]

    graph[start][end] = 0
    graph[end][start] = 0

    if is_existed(graph, start) and is_existed(graph, end):
        del new_arr[index]
    else:
        graph[start][end] = save_cost
        graph[end][start] = save_cost
        index += 1

print("## 가장 효율적인 해저 케이블 연결도 ##")
print_graph(graph)