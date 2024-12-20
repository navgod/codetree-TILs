import sys

INT_MIN = -sys.maxsize

n = int(input())

array = list(map(int,input().split()))
dp = [INT_MIN]*n
dp[0] = 0

for i in range(1,n):
    for j in range(i):
        if dp[j] == INT_MIN:
            continue
        
        if array[j] +j >= i:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))