import sys

def two_sum (a, b, carry=0) :

    if not a and not b and carry == 0:
        return ''
    

    if not a:
        a = '0'
    if not b:
        b = '0'

    sum_val = int(a[-1]) + int(b[-1]) + carry
    
    # 덧셈 후 2로 나눈 나머지
    digit = str(sum_val % 2)
    
    # 자리 올림 계산
    carry = sum_val // 2
    
    # 재귀 호출로 나머지 자리를 더함
    return two_sum(a[:-1], b[:-1], carry) +digit

a, b =sys.stdin.readline().strip().split()

result = two_sum(a, b).lstrip('0')
if result == '':
    result = '0'
print(result)