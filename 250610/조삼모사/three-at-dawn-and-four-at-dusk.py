from itertools import combinations

n = int(input())
P = [list(map(int, input().split())) for _ in range(n)]

total = [i for i in range(n)]
min_diff = float('inf')


for comb in combinations([i for i in range(n)], n//2): 
    day = 0
    for i in range(n//2):
        for j in range(n//2):
            day += P[comb[i]][comb[j]]
    night_set = [i for i in range(n) if i not in comb]
    night = 0
    for i in range(n//2):
        for j in range(n//2):
            night += P[night_set[i]][night_set[j]]
    min_diff = min(min_diff, abs(night - day))
    
print(min_diff)