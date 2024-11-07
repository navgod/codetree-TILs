n,m = map(int, input().split())

jewel = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (m+1) # 질량이 m을 담을 수 있는 최대 가치
dp[0] = 1

def is_range(x):
    return 0<=x<=m

# initialize
for w,v in jewel:
    for i in range(m,-1,-1):
        if is_range(i-w) and dp[i-w]:
            dp[i] = max(dp[i],dp[i-w] + v)

print(max(dp)-1)