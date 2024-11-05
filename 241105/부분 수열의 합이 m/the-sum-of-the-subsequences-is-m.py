n,m = map(int, input().split())

array = list(map(int, input().split()))


dp = [10001]*(m+1)
dp[0] = 0

def is_range(x):
    return 0<=x<=m

for num in array:
    for i in range(m,-1,-1):
        if is_range(i-num) and dp[i-num] != -1:
            dp[i] = min(dp[i],dp[i-num]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])