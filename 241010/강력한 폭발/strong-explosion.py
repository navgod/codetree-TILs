n = int(input())

grid = [list(map(int , input().split())) for _ in range(n)]

ans = 0

case1 = [
    (0,-2),
    (0,-1),
    (0,0),
    (0,1),
    (0,2)
    ]
case2 = [
    (-1,0),
    (0,-1),
    (0,0),
    (1,0),
    (0,1)
    ]
case3 = [
    (-1,-1),
    (1,-1),
    (0,0),
    (1,1),
    (-1,1)
    ]
bomb = []

coord = set()

for x in range(n):
    for y in range(n):
        if grid[y][x] == 1:
            bomb.append((x,y))

def is_range(x,y):
    return 0<=x<n and 0<=y<n

def counting(idx):
    global ans, coord

    if idx == len(bomb):
        ans = max(ans,len(coord))
        return
    
    x,y = bomb[idx]

    added_coords = []
    for dx, dy in case1:
        nx, ny = x + dx, y + dy
        if is_range(nx, ny) and (nx, ny) not in coord:
            coord.add((nx, ny))
            added_coords.append((nx, ny))
    counting(idx + 1)

    for cx, cy in added_coords:
        coord.remove((cx, cy))

    added_coords = []
    for dx, dy in case2:
        nx , ny = x+dx, y+dy
        if is_range(nx,ny) and (nx, ny) not in coord:
            coord.add((nx,ny))
            added_coords.append((nx, ny))


    counting(idx+1)
    for cx, cy in added_coords:
        coord.remove((cx, cy))

    added_coords = []
    for dx, dy in case3:
        nx , ny = x+dx, y+dy
        if is_range(nx,ny)and (nx, ny) not in coord:
            coord.add((nx,ny))
            added_coords.append((nx, ny))

    counting(idx+1)
    for cx, cy in added_coords:
        coord.remove((cx, cy))


counting(0)
print(ans)