n = int(input())
speed = [int(input()) for _ in range(n)]

def merged_sort(arr, temp, left, right):
    if left >= right:
        return 0
    mid = (left + right) // 2
    inv_count = merged_sort(arr, temp, left, mid) + merged_sort(arr, temp, mid + 1, right)

    i, j, k = left, mid + 1, left
    while i <= mid and j <= right:
        if arr[i] >= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp[i]

    return inv_count

temp = [0] * n
print(merged_sort(speed, temp, 0, n - 1))