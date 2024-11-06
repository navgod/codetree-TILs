n,m = map(int ,input().split())
array = list(map(int ,input().split()))


dp = [0]*(m+1)
dp[0] = 1
for arr in array:
    for i in range(m,-1,-1):
        if i-arr <0:
            break
        
        if dp[i-arr]:
            dp[i] = dp[i-arr]

if dp[m]:
    print("Yes")
else:
    print("No")