n = int(input())

dp = [0] *(n+10)

dp[2] = 1
dp[3] = 1
dp[4] = 1
dp[5] = 2
dp[6] = 2
for i in range(7,n+1):
    dp[i] = (dp[i-2] + dp[i-3])%10007
print(dp[n])