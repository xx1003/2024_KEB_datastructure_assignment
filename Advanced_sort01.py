import random
import time

arr1 = [random.randint(0, 1000) for _ in range(1000)]
arr2 = [random.randint(0, 10000) for _ in range(10000)]
arr3 = [random.randint(0, 10000) for _ in range(12000)]
arr4 = [random.randint(0, 10000) for _ in range(15000)]


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        min_num = arr[i]
        for j in range(i, len(arr)):
            if arr[j] < min_num:
                min_num = arr[j]
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def quick_sort(arr, start, end):
    if end <= start:
        return arr

    low = start
    high = end
    mid = (low + high) // 2

    while low <= high:
        while arr[low] < arr[mid]:
            low += 1
        while arr[high] > arr[mid]:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1

    mid = low
    quick_sort(arr, start, mid - 1)
    quick_sort(arr, mid, end)

    return arr


def print_perform(arr):
    print(f"## amount of data : {len(arr)}")
    start = time.time()
    selection_sort(arr)
    end = time.time()
    print(f"    selection sort --> {round(end - start, 3)} second")
    start = time.time()
    quick_sort(arr, 0, len(arr)-1)
    end = time.time()
    print(f"    quick sort -->  {round(end - start, 3)} second")
    print()


print_perform(arr1)
print_perform(arr2)
print_perform(arr3)
print_perform(arr4)



