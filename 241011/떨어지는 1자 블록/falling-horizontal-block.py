n,m,k = map(int , input().split())
k -=1
grid = [list(map(int , input().split())) for _ in range(n)]

now_row = -1

def fall_down():
    global now_row
    stop = False
    next_row = now_row +1
    if next_row >= n:
        return
    for i in range(k,k+m):
        if grid[next_row][i] !=0:
            stop = True
            break
    if not stop:
        now_row = next_row
        fall_down()

fall_down()
for i in range(k,k+m):
    grid[now_row][i] = 1
for row in grid:
    for col in row:
        print(col, end =' ')
    print()