from itertools import groupby
n = input()
result = []
for char, group in groupby(n):
    count = len(list(group))
    result.append(f"({count}, {char})")
print(' '.join(result))    
