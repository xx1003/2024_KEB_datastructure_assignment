graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 1, 1, 0, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0]
]
       #    0      1       2          3           4
store = ['GS25', 'CU', 'Seven11', 'MiniStop', 'Emart24']
honey_butter = [30, 60, 10, 90, 40]
visited = [0] * len(store)

def print_graph():
    print("## 편의점 그래프 ##")
    print("                ", end='')
    for s in store:
        print(f"{s:10s}", end=' ')
    print()
    for i in range(len(store)):
        print(f"{store[i]:10s}", end='')
        for j in range(len(store)):
            print(f"{graph[i][j]:10d}", end='')
        print()


MAX = honey_butter[0]
max_store = 0

def dfs(g, i):
    global MAX, max_store, visited
    visited[i] = 1
    if MAX <= honey_butter[i]:
        MAX = honey_butter[i]
        max_store = i
    for j in range(len(store)):
        if g[i][j] == 1 and visited[j] == 0:
            dfs(g, j)


print_graph()
dfs(graph, 0)
print(f"허니버터칩 최대 보유 편의점(개수) --> {store[max_store]} ( {MAX} )")