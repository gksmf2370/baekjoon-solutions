import sys

def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i ==0:
            return False
    return True
n_list = list(range(1,246913))
prime_list =[]
for i in n_list:
    if is_prime(i):
        prime_list.append(i)

while True:
    a= int(sys.stdin.readline().strip())
    if a ==0:
        break

    count=0
    for i in prime_list:
        if a < i <= 2*a:
            count += 1
    print(count)

