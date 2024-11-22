import sys

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False] 
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            is_prime[i * i : limit + 1 : i] = [False] * len(range(i * i, limit + 1, i))
    return is_prime

def find_goldbach_partition(n, is_prime):
    for a in range(n // 2, 1, -1):
        b = n - a
        if is_prime[a] and is_prime[b]:
            return a, b

input_data = sys.stdin.read().split()
T = int(input_data[0])
numbers = map(int, input_data[1:])

is_prime = sieve_of_eratosthenes(10000)

results = []
for n in numbers:
    a, b = find_goldbach_partition(n, is_prime)
    results.append(f"{a} {b}")

print("\n".join(results))

