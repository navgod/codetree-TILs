def is_range(x,y):
    return 0<=x<n and 0<=y<n

def move():
    new_beads = []
    for bead in beads:
        x,y,d,w,idx = bead
        dx,dy = dxs[d], dys[d]
        if is_range(x+dx,y+dy):
            nx,ny = x+dx,y+dy
        else:
            nx,ny = x,y
            d = (d+2)%4
        new_beads.append([nx,ny,d,w,idx])

    return new_beads

def check():
    new_beads = []
    for x,y,d,w,idx in beads:
        grid[y][x].append(w)
        next_grid[y][x] = idx
        filled[y][x] = 0
    for x,y,d,w,idx in beads:
        if len(grid[y][x]) == 1:
            if not filled[y][x]:
                new_beads.append([x,y,d,w,idx])
                grid[y][x] = []
                next_grid[y][x] = -1
                filled[y][x] = 1
        else:
            if not filled[y][x]:
                new_w = sum(grid[y][x])
                new_idx = next_grid[y][x]
                new_d = beads[new_idx][2]
                new_beads.append([x,y,new_d,new_w,new_idx])
                grid[y][x] = []
                next_grid[y][x] = -1
                filled[y][x] = 1

    return new_beads

dir_map = {
    'U':0,
    'L':1,
    'D':2,
    'R':3
}
dxs,dys = [0,-1,0,1] , [-1,0,1,0]
n,m,t = map(int, input().split())
grid = [[[] for _ in range(n)] for _ in range(n)]
next_grid = [[-1]*n for _ in range(n)]
filled = [[0]*n for _ in range(n)]

beads = []

for idx in range(m):
    x = input().split()
    beads.append([int(x[1])-1,int(x[0])-1,dir_map[x[2]],int(x[3]),idx])

for _ in range(t):
    beads = move()
    beads = check()

weights = sorted(beads, key = lambda x: x[3])

print(len(beads),weights[-1][3])