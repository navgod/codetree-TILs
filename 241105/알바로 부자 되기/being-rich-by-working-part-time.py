n = int(input())

part_timer = [list(map(int, input().split())) for _ in range(n)]

dp_up = [0]*n
dp_down = [0]*n
dp = [0]*n
for i in range(n):
    s, e, p = part_timer[i]
    dp_up[i] += p
    for j in range(i):
        j_s, j_e , j_p = part_timer[j]
        if j_e <= s:
            dp_up[i] = max(dp_up[i],dp_up[j])
for i in range(n-1,-1,-1):
    s, e, p = part_timer[i]
    dp_down[i] += p
    for j in range(i+1,n):
        j_s, j_e , j_p = part_timer[j]
        if j_s >= e:
            dp_down[i] = max(dp_down[i],dp_down[j])
    
for i in range(n):
    dp[i] = dp_up[i] + dp_down[i] - part_timer[i][2]

print(max(dp))