import sys

def is_prime(n):
    if n<2:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

n_list = list(range(1,1000000))
prime_list=[]

for i in n_list:
    if is_prime(i):
        prime_list.append(i)


a = int(sys.stdin.readline().strip())

for _ in range(a):
    b = int(sys.stdin.readline().strip())
    c=0
    for i in range(2,b//2 +1):
        x = b-i
        if (i in prime_list) and (x in prime_list):
            c +=1
    print(c)

## chat gpt 코드   
import sys

def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False
                
    return is_prime

max_num = 1000000
is_prime = sieve_of_eratosthenes(max_num)

a = int(sys.stdin.readline().strip())

for _ in range(a):
    b = int(sys.stdin.readline().strip())
    c = 0
    for i in range(2, b // 2 + 1):
        if is_prime[i] and is_prime[b - i]:
            c += 1
    print(c)