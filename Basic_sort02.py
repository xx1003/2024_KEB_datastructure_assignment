arr = [
    [55, 33, 250, 44],
    [88, 1, 76, 23],
    [199, 222, 38, 47],
    [155, 145, 20, 99]
]

arr2 = []

for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr2.append(arr[i][j])

print(f"after changing 2d array to 1d array, before sorting --> {arr2}")


def selection_sort():
    global arr2
    for start in range(len(arr2)-1):
        min_num = arr2[start]
        min_idx = start
        for cur in range(start, len(arr2)):
            if arr2[cur] < min_num:
                min_num = arr2[cur]
                min_idx = cur
        arr2[start], arr2[min_idx] = arr2[min_idx], arr2[start]


def insertion_sort():
    global arr2
    for end in range(1, len(arr2)):
        for cur in range(end, 0, -1):
            if arr2[cur] < arr2[cur - 1]:
                arr2[cur], arr2[cur - 1] = arr2[cur - 1], arr2[cur]


# selection_sort()
insertion_sort()
print(f"after changing 2d array to 1d array, after sorting --> {arr2}")
print(f"median value --> {arr2[len(arr2)//2]}")
