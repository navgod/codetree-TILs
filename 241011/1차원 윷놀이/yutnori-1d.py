n,m,k = map(int , input().split())

moves = list(map(int , input().split()))

doll = [1 for _ in range(k)]

ans = 0
def move(idx):
    global ans
    if idx == n:
        cnt = 0
        for i in doll:
            if i >= m:
                cnt+=1
        ans = max(ans ,cnt)
        return
    
    for i in range(k):
        doll[i] += moves[idx]
        move(idx+1)
        doll[i] -= moves[idx]
move(0)
print(ans)