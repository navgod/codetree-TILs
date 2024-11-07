n = int(input())
prices = list(map(int, input().split()))

dp = [0]*(n+1)
dp[1] = prices[0]

for leng in range(2,n+1):
    for cut in range(1,leng+1):
        dp[leng] = max(dp[leng-cut] + prices[cut-1], dp[leng])

print(dp[n])