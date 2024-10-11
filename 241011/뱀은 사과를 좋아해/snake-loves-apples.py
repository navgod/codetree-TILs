from collections import deque

n,m,k = map(int,input().split())

grid = [[0]*n for _ in range(n)]

snake = deque()

head = (0,0)

snake.appendleft(head)
apples = []
for _ in range(m):
    x,y = map(int , input().split())
    x, y = y-1, x-1
    grid[y][x] = 1

command = []

dir_dict = {
    'U':0,
    'D':1,
    'R':2,
    'L':3
}
dxs ,dys = [0,0,1,-1] , [-1,1,0,0]
for _ in range(k):
    d, p = input().split()
    command.append((dir_dict[d],int(p)))

t= 0 

def is_range(x,y):
    return 0<= x<n and 0<=y<n

def can_go(x,y):
    return is_range(x,y) and grid[y][x] !=2

def eat_apple(x,y):
    global grid
    if grid[y][x] == 1:
        grid[y][x] = 0
        return True
    else:
        return False

def game():
    global t
    x,y = head
    grid[0][0] = 2
    for dir , dura in command:
        for i in range(1,dura+1):
            nx, ny = x+dxs[dir] , y+dys[dir]
            if not can_go(nx,ny): # game over
                t+=1
                return
            snake.appendleft((nx,ny))
            if not eat_apple(nx,ny):
                last_x, last_y = snake.pop()
                grid[last_y][last_x] = 0
            grid[ny][nx] = 2
            x,y = nx,ny
            t+=1

game()
print(t)