n,m = map(int , input().split())
nums = list(map(int , input().split()))

selected = []
ans = 0
def choose(idx,cnt):
    global ans
    if idx ==n:
        if cnt == m:
            keep = None
            for i in selected:
                if keep:
                    keep = keep^i
                else:
                    keep = i
            ans = max(ans,keep)
        return
    selected.append(nums[idx])
    choose(idx+1,cnt+1)
    selected.pop()
    choose(idx+1,cnt)

choose(0,0)
print(ans)