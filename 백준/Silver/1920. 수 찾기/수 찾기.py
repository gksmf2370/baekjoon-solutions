import sys

def binary_search(target, data):
    start = 0
    end = len(data) -1

    while start<=end :
        mid = (start + end) //2
        if data[mid] == target:
            return 1           # 타겟이 있으면 1
        elif data[mid] < target:
            start = mid+1
        else:
            end = mid- 1
    return 0                  # 타겟이 없으면 0


a=int(sys.stdin.readline().strip())
b = list(map(int,sys.stdin.readline().strip().split()))
c=int(sys.stdin.readline().strip())
d = list(map(int,sys.stdin.readline().strip().split()))

# 이진 탐색을 할때는 정렬을 해줘야한다.
b.sort()

for i in d:
    result = binary_search(i,b)
    print(result)