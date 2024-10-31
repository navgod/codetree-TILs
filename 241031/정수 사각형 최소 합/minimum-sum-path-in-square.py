n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

dp[0][n-1] = grid[0][n-1]
for col in range(n-2,-1,-1):
    dp[0][col] += dp[0][col+1] + grid[0][col]
for row in range(1,n):
    dp[row][n-1] += dp[row-1][n-1] + grid[row][n-1]
for row in range(1,n):
    for col in range(n-2,-1,-1):
        dp[row][col] = min(dp[row-1][col],dp[row][col+1])+ grid[row][col]

print(dp[n-1][0])