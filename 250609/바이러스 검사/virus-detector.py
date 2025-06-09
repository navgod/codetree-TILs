from math import ceil
n = int(input())
customers = list(map(int,input().split()))
L,M = map(int,input().split())
print(sum( [ceil((c-L)/M)+1 if c>L else 1 for c in customers]))