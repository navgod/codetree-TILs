n = int(input())

dp = [0]*(n+1)
dp[0] = 1
def is_range(x):
    return 0<= x<=n

for i in range(n+1):
    if is_range(i+1):
        dp[i+1] += dp[i]
    if is_range(i+2):
        dp[i+2] += dp[i]
    if is_range(i+5):
        dp[i+5] += dp[i]

print(dp[n]%10007)