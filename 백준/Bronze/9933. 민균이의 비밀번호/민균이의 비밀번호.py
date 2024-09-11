import sys

a = int(sys.stdin.readline().strip())
words = [sys.stdin.readline().strip() for _ in range(a)] 


for word in words:
    reversed = word[::-1] 

    if reversed in words:
        length = len(word)
        mid_char = word[length // 2]  # 중간 글자
        print(f"{length} {mid_char}")
        break
