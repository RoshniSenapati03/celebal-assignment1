from itertools import combinations

n = int(input())
letter = input().split()
k = int(input())

all_combine = list(combinations(letter,k))
count_a = 0
for combi in all_combine:
    if 'a' in combi:
        count_a += 1
total = len(all_combine)
probability = count_a / total
print (round(probability, 4))
       
