n = int(input())
mod = 1000000007
dp = [0] * (n+2)
dp[1] = 2
dp[2] = 7

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] * 2 + dp[i - 2] * 3) % mod
    for j in range(i - 3, -1, -1):
        dp[i] = (dp[i] + dp[j] * 2) % mod

print(dp[n]%mod)