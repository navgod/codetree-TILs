n,m = map(int , input().split())

dp = [0]*(m+1)
dp[m] = -1

coins = list(map(int , input().split()))

def is_range(x):
    return 0<=x<=m

for coin in coins:
    if is_range(coin):
        dp[coin] = 1

for i in range(m+1):
    for coin in coins:
        if is_range(i-coin):
            dp[i] = max(dp[i],dp[i-coin]+1)
            
print(dp[m])