n = int(input())
array = list(map(int , input().split()))
dp = [0]*n
dp[0] = 1
for i in range(1,n):
    for j in range(0,i):
        if array[i]> array[j]:
            dp[i] = max(dp[j]+1,dp[i])

print(dp[n-1])