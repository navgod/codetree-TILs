n,m = map(int, input().split())
coins = list(map(int, input().split()))

dp = [10001]*(m+1)
def is_range(x):
    return 0<=x<=m

for coin in coins:
    if is_range(coin):
        dp[coin] =1

for i in range(m+1):
    for coin in coins:
        if is_range(coin) and is_range(i-coin):
            if dp[i-coin]:
                dp[i] = min(dp[i],dp[i-coin]+1)

print(dp[m])