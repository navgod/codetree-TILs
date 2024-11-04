n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]

# 최대 최소
dp = [[[0,0] for _ in range(n)] for _ in range(n)]

dp[0][0][0], dp[0][0][1] = grid[0][0] , grid[0][0]

for row in range(1,n):
    dp[row][0][0] = max(dp[row-1][0][0],grid[row][0])
    dp[row][0][1] = min(dp[row-1][0][1],grid[row][0])

for col in range(1,n):
    dp[0][col][0] = max(dp[0][col-1][0],grid[0][col])
    dp[0][col][1] = min(dp[0][col-1][1],grid[0][col])

for row in range(1,n):
    for col in range(1,n):
        now = grid[row][col]
        # 위의 경우
        up_max = dp[row-1][col][0]
        up_min = dp[row-1][col][1]
        ups = [now,up_max,up_min]
        # 왼쪽의 경우
        left_max = dp[row][col-1][0]
        left_min = dp[row][col-1][1]
        lefts = [now,left_max,left_min]

        if (max(ups)-min(ups)) >= (max(lefts)-min(lefts)):
            dp[row][col][0],dp[row][col][1]  = max(lefts) , min(lefts)
        else:
            dp[row][col][0],dp[row][col][1]  = max(ups) , min(ups)


print(dp[n-1][n-1][0]-dp[n-1][n-1][1])