from collections import deque

n,m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]

north, east, south, west = (-1,0) , (0,1) , (1,0) , (0,-1)

player = []


min_area = float('inf')
dir_queue = deque()

directions = [
    [[north],[west],[south],[west]],
    [[west,east],[north,south]],
    [[north,east],[west,north],[south,west],[east,south]],
    [[west,north,east],[south,west,north],[east,south,west],[north,east,south]],
    [[north,east,west,south]]
]

for i in range(n):
    for j in range(m):
        if 0 < board[i][j] < 6:
            player.append((i,j,len(directions[board[i][j]-1])))
        
num_player = len(player)
def is_range(r,c):
    return 0<= r < n and 0<= c < m

def cal_area(board):
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = deque()

    for idx, (i,j, _) in enumerate(player):
        for dr , dc in dir_queue[idx]:
            queue.append((i,j,dr,dc))
    while queue:
        r,c,dr,dc = queue.popleft()
        while is_range(r+dr,c+dc) and board[r+dr][c+dc] !=6:
            r , c = r +dr , c +dc
            visited[r][c] = True

    return sum([
        1
         for i in range(n)
         for j in range(m)
         if not visited[i][j] and board[i][j] == 0
    ])


## 말이 하나도 없는 경우는 없다고 가정

def dfs(depth):
    if depth == num_player:
        global min_area
        area = cal_area(board)
        min_area = min(min_area,area)
        return
    now_player = player[depth]
    for i in range(now_player[2]):
        dir_queue.append(directions[board[now_player[0]][now_player[1]]-1][i]) #방향들일수도 방향 하나 일수도
        dfs(depth+1)
        dir_queue.pop()

dfs(0)
print(min_area)