from itertools import combinations

while True:
    
    data = list(map(int, input().split()))
    if data[0] == 0:  
        break
    
    
    k = data[0]
    s = data[1:]
    
    
    for combination in combinations(s, 6):
        print(" ".join(map(str, combination)))
    
    print()
