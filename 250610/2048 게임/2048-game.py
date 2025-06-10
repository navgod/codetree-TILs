n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

Max_Moves = 5
ans = -1

def move_board(board, dir):

    new_board = [row[:] for row in board]

    if dir == 0: # 위로
        for col in range(n):
            merged = [False for _ in range(n)]
            for row in range(1,n):
                if new_board[row][col]:
                    r= row
                    while 0 < r and new_board[r-1][col] ==0:
                        new_board[r-1][col] , new_board[r][col] = new_board[r][col] , new_board[r-1][col]
                        r -=1
                    if r !=0 and not merged[r-1] and new_board[r][col] == new_board[r-1][col]:
                        new_board[r-1][col] = new_board[r][col] *2
                        new_board[r][col] = 0
                        merged[r-1] = True
    elif dir == 1: # 아래로
        for col in range(n):
            merged = [False for _ in range(n)]
            for row in range(n-2,-1,-1):
                if new_board[row][col]:
                    r = row
                    while r < n -1 and new_board[r+1][col] ==0:
                        new_board[r+1][col] , new_board[r][col] = new_board[r][col] , new_board[r+1][col]
                        r +=1
                    if r != n-1 and not merged[r+1] and new_board[r][col] == new_board[r+1][col]:
                        new_board[r+1][col] = new_board[r][col] *2
                        new_board[r][col] = 0
                        merged[r+1] = True
    elif dir == 2: # 오른쪽
        for row in range(n):
                merged = [False for _ in range(n)]
                for col in range(n-2,-1,-1):
                    if new_board[row][col]:
                        c = col
                        while c < n-1 and new_board[row][c+1] ==0:
                            new_board[row][c+1] , new_board[row][c] = new_board[row][c] , new_board[row][c+1]
                            c += 1
                        if c !=n-1 and not merged[c+1] and new_board[row][c] == new_board[row][c+1]:
                            new_board[row][c+1] = new_board[row][c] *2
                            new_board[row][c] = 0
                            merged[c+1] = True
    else: # 왼쪽
        for row in range(n):
            merged = [False for _ in range(n)]
            for col in range(1,n):
                if new_board[row][col]:
                    c = col
                    while 0 < c  and new_board[row][c-1] ==0:
                        new_board[row][c-1] , new_board[row][c] = new_board[row][c] , new_board[row][c-1]
                        c -= 1
                    if c != 0 and not merged[c-1] and new_board[row][c] == new_board[row][c-1]:
                        new_board[row][c-1] = new_board[row][c] *2
                        new_board[row][c] = 0
                        merged[c-1] = True

    return new_board

def get_max(board):
    return max(
        [
            board[i][j]
            for i in range(n)
            for j in range(n)
        ]
    )

def dfs(board, moves):
    global ans

    if moves == Max_Moves:
        ans = max(ans, get_max(board))
        return

    for dir in range(4):
        new_board = move_board(board, dir)
        dfs(new_board, moves +1)

dfs(board,0)
print(ans)