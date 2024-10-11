n,m = map(int, input().split())

points = [list(map(int, input().split())) for _ in range(n)]

selected = []

ans = 1000000000

def calc():
    max_diff =0
    for i in range(m):
        for j in range(i+1,m):
            x1, y1 = selected[i]
            x2, y2 = selected[j]
            max_diff = max(max_diff, (x1-x2)**2+(y1-y2)**2 )
    return max_diff

def choose(idx,cnt):
    global ans
    if idx == n:
        if cnt ==m:
            ans = min(ans , calc())
        return
    if cnt<m:
        selected.append(points[idx])
        choose(idx+1,cnt+1)
        selected.pop()
    choose(idx+1,cnt)

choose(0,0)

print(ans)