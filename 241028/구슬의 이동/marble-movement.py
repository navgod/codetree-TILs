dir_map = {
    'U':0,
    'D':2,
    'R':1,
    'L':3
}
dxs,dys = [0,1,0,-1] , [-1,0,1,0]

def is_range(x,y):
    return 0<=x<n and 0<=y<n

def move(bead):
    r,c,d,v = bead
    x,y = c-1,r-1
    dx,dy = dxs[d], dys[d]
    for i in range(v):
        if not is_range(x+dx,y+dy):
            d = (d+2)%4
            dx,dy = dxs[d], dys[d]
        x,y = x+dx, y+dy
    return [y+1,x+1,d,v]

def check():
    # 속도가 큰순위 같으면 idx가 큰순위
    idx = 0
    n_beads = []
    for r,c,d,v in beads:
        grid[r-1][c-1].append((v,idx))
        idx+=1
    for x in range(n):
        for y in range(n):
            if len(grid[y][x]) >k:
                target = grid[y][x]
                selected_beads = sorted(target, key= lambda x: (x[0],x[1]), reverse = True)
                for i in range(k):
                    n_idx = selected_beads[i][1]
                    n_beads.append(beads[n_idx])
            else:
                if grid[y][x]:
                    for v,i in grid[y][x]:
                        if i>= len(beads):
                            print(i, len(beads), beads)
                        else:
                            n_beads.append(beads[i])
            grid[y][x].clear()
    return n_beads


n,m,t,k = map(int, input().split())
beads = [[int(x[0]), int(x[1]), dir_map[x[2]], int(x[3])] for x in (input().split() for _ in range(m))]
grid = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(t):
    new_beads = []
    for bead in beads:
        new_bead = move(bead)
        new_beads.append(new_bead)
    beads = new_beads
    beads = check()

print(len(beads))