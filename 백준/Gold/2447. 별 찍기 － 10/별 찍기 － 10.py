import sys
# 27개 , 3^n 승
def draw_star(n):
    if n ==1:
        return '*'
    
    star = draw_star(n//3)  # 재귀
    result = [] #배열로 저장
    for i in range(n):
        if (i // (n//3)) ==1:
            result.append(star[i%(n//3)] + ' ' *(n//3) + star[i%(n//3)]) # 두번째에는 공백도들어감
            continue
        result.append(star[i%(n//3)] * 3)
    return result

a = int(sys.stdin.readline().strip())
result = draw_star(a)
for i in result:
    print(i)