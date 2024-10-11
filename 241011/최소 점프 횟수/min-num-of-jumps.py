n = int(input())
jumps = list(map(int , input().split()))

visited= [0]*n
ans = n+1
def jump(x):
    global ans
    if x >= n-1:
        if x== n-1:
            ans = min(ans,sum(visited))
        return
    for i in range(1,jumps[x]+1):
        if x+i <n:
            visited[x+i] =1
            jump(x+i)
            visited[x+i] =0
    
jump(0)

print(ans if ans <n else -1)