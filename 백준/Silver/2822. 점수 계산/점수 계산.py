import sys
scores =[]
for _ in range(8):
    a= int(sys.stdin.readline().strip())
    scores.append(a)

indexed_scores = [(score, idx + 1) for idx, score in enumerate(scores)]

top = sorted(indexed_scores, reverse=True, key=lambda x: x[0])[:5]

total_score = sum([score[0] for score in top])

indices = sorted([score[1] for score in top])


print(total_score)
print(' '.join(map(str, indices)))