import sys
input=sys.stdin.readline
def longest_bitonic_subsequence(arr):
    n = len(arr)

    # LIS 배열 초기화
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                lis[i] = max(lis[i], lis[j] + 1)

    
    lds = [1] * n
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                lds[i] = max(lds[i], lds[j] + 1)

    
    max_length = 0
    for i in range(n):
        max_length = max(max_length, lis[i] + lds[i] - 1)

    return max_length


n = int(input())
arr = list(map(int, input().split()))


print(longest_bitonic_subsequence(arr))
