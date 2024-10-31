n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

dp[0][0] = grid[0][0]
for col in range(1,n):
    dp[0][col] = min(dp[0][col-1],grid[0][col])
for row in range(1,n):
    dp[row][0] = min(dp[row-1][0] , grid[row][0])
for row in range(1,n):
    for col in range(1,n):
        before_min = min(dp[row-1][col],dp[row][col-1])
        if before_min >= grid[row][col]:
            dp[row][col] = grid[row][col]
        else:
            before_max = max(dp[row-1][col],dp[row][col-1])
            if before_max >= grid[row][col]:
                dp[row][col] = grid[row][col]
            else:
                dp[row][col] = before_max
print(dp[n-1][n-1])