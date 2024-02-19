arr = [['sunmi', 88], ['choa', 99], ['hwasa', 71], ['youngtak', 78],
       ['youngong', 67], ['minho', 92]]


def selection_sort():
    global arr
    for i in range(len(arr)-1):
        min_num = arr[i][1]
        min_idx = i
        for j in range(i, len(arr)):
            if arr[j][1] < min_num:
                min_num = arr[j][1]
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def insertion_sort():
    global arr
    for i in range(1, len(arr)-1):
        for j in range(i, 0, -1):
            if arr[j][1] < arr[j-1][1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr


print(f"before sorting --> {arr}")
print(f"after sorting --> {selection_sort()}")
# print(f"after sorting --> {insertion_sort()}")

print("## Teammate by test score ##")
for i in range(len(arr)//2):
    print(f"{arr[0]} : {arr[-1]}")
    arr = arr[1:-1]




