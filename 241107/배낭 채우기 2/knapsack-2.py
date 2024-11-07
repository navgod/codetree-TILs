n,m = map(int , input().split())
jewel = [list(map(int , input().split())) for _ in range(n)]

dp = [0] * (m+1)
def is_range(x):
    return 0<x<=m
for w,v in jewel:
    if is_range(w):
        dp[w] = max(dp[w],v)


for weight in range(1,m+1):
    for w,v in jewel:
        times = 1
        tmp = weight - w
        while is_range(tmp):
            dp[weight] = max(dp[weight], dp[tmp] + v * times)
            times +=1
            tmp -= w

print(max(dp))