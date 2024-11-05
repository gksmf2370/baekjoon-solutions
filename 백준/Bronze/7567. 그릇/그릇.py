bowls = input().strip()  

total_height = 10
previous_bowl = bowls[0]
for i in range(1, len(bowls)):
    current_bowl = bowls[i]
    if current_bowl == previous_bowl:
        total_height += 5
    else:
        total_height += 10
    previous_bowl = current_bowl

print(total_height)
