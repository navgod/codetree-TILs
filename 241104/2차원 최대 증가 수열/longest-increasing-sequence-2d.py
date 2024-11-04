n,m = map(int , input().split())
grid = [list(map(int , input().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]
dp[0][0] = 1

row, col = 0,0

for r in range(1,n):
    for c in range(1,n):
        for l_r in range(r):
            for l_c in range(c):
                if grid[r][c] > grid[l_r][l_c] and dp[l_r][l_c]>0:
                    dp[r][c] = max(dp[r][c],dp[l_r][l_c]+1)
ans = 0

for row in dp:
    for col in row:
        ans = max(ans,col)
print(ans)