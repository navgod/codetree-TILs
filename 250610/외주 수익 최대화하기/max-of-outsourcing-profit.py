n = int(input())
duration =[]
profit = []

for _ in range(n):
    t,p = map(int,input().split())
    duration.append(t)
    profit.append(p)
ans = -1

def dfs(day,accum):
    if day == n:
        global ans
        ans = max(ans,accum)
        return
    if day + duration[day] <= n:
        dfs(day+duration[day],accum + profit[day])
    dfs(day+1,accum)

dfs(0,0)
print(ans)