from itertools import combinations

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

min_diff = float('inf')

for team in combinations(range(n), n // 2):
    start_team = set(team)
    link_team = set(range(n)) - start_team

    start_score = 0
    link_score = 0

    for i in start_team:
        for j in start_team:
            start_score += s[i][j]
    
    for i in link_team:
        for j in link_team:
            link_score += s[i][j]
    
    diff = abs(start_score - link_score)
    min_diff = min(min_diff, diff)

print(min_diff)
