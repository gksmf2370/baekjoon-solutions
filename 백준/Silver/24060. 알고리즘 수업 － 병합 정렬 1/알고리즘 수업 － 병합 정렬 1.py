import sys

def merge_sort(arr, tmp, l, r, k, cnt_res):
    if l < r:
        m = (l + r) // 2
        cnt_res = merge_sort(arr, tmp, l, m, k, cnt_res)
        cnt_res = merge_sort(arr, tmp, m + 1, r, k, cnt_res)
        cnt_res = merge(arr, tmp, l, m, r, k, cnt_res)
    return cnt_res

def merge(arr, tmp, l, m, r, k, cnt_res):
    cnt, res = cnt_res
    i, j, idx = l, m + 1, l

    while i <= m and j <= r:
        if arr[i] <= arr[j]:
            tmp[idx] = arr[i]
            i += 1
        else:
            tmp[idx] = arr[j]
            j += 1
        idx += 1
        cnt += 1
        if cnt == k:
            res = tmp[idx - 1]

    while i <= m:
        tmp[idx] = arr[i]
        i += 1
        idx += 1
        cnt += 1
        if cnt == k:
            res = tmp[idx - 1]

    while j <= r:
        tmp[idx] = arr[j]
        j += 1
        idx += 1
        cnt += 1
        if cnt == k:
            res = tmp[idx - 1]

    for i in range(l, r + 1):
        arr[i] = tmp[i]
        
    return cnt, res
n, k = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
tmp = [0] * n
cnt_res = (0, -1) 
_, result = merge_sort(arr, tmp, 0, n - 1, k, cnt_res)

print(result)