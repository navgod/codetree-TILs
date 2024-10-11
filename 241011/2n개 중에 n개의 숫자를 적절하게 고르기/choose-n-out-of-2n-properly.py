n = int(input())
nums = list(map(int , input().split()))

selected = []

target = sum(nums)
ans = target +1
def select(idx,cnt):
    global ans
    if idx == 2*n:
        if cnt == n:
            ans = min(ans,abs(target -2*sum(selected)))
        return
    
    if cnt <n:
        selected.append(nums[idx])
        select(idx+1,cnt+1)
        selected.pop()
    select(idx+1,cnt)
    
select(0,0)

print(ans)