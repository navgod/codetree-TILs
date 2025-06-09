n,m = map(int,input().split())
r,c,d = map(int,input().split())
road = [list(map(int,input().split())) for _ in range(n)]

directions = [(-1,0),(0,1),(1,0),(0,-1)]
visited = [[False for _ in range(m)] for _ in range(n)]

visited[r][c] = True

def is_range(r,c):
    return 0<= r < n and 0<= c < m

def turn_left(before_dir):
    return (before_dir-1)%4

def move(r,c,d):
    moved = False
    di = d
    for _ in range(4):
        di = turn_left(di)
        nr, nc = r+ directions[di][0], c+ directions[di][1]
        if is_range(nr,nc) and not visited[nr][nc] and road[nr][nc] == 0:
            visited[nr][nc] = True
            return (nr,nc,di)
    return (r,c,d)

while True:
    nr,nc,nd = move(r,c,d)

    if (nr,nc) == (r,c):
        nr,nc = r - directions[d][0] , c - directions[d][1]
        if not is_range(nr,nc) or road[nr][nc] == 1:
            break
        else:
            r ,c = nr,nc
    else:
        r,c,d = nr,nc,nd
move(r,c,d)
print(sum([1 for i in range(n) for j in range(m) if visited[i][j] == True]))
