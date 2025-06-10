class Dice:               #                  0
    def __init__(self): # 형상을 1(bottom) 2 3(top) 4 
                      #                      5 으로 가정 위부터 아래로, 왼쪽부터 오른쪽으로 인덱싱
        self.numbers = [0 for _ in range(6)]
    def dice_to_board(self):
        return self.numbers[1]
    def board_to_dice(self,num):
        self.numbers[1] = num
    def roll_south(self):
        self.numbers[0], self. numbers[3], self.numbers[5], self.numbers[1] =  self.numbers[1], self.numbers[0], self.numbers[3], self.numbers[5]
    def roll_north(self):
        self.numbers[0], self. numbers[3], self.numbers[5], self.numbers[1] =  self.numbers[3], self.numbers[5], self.numbers[1], self.numbers[0]
    def roll_east(self):
        self.numbers[1], self. numbers[2], self.numbers[3] , self.numbers[4] = self.numbers[4], self.numbers[1], self.numbers[2], self.numbers[3]
    def roll_west(self):
        self.numbers[1], self. numbers[2], self.numbers[3] , self.numbers[4] = self.numbers[2], self.numbers[3], self.numbers[4], self.numbers[1]


n,m,x,y,k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
rolling = list(map(int, input().split()))
dice = Dice()

def is_range(x,y):
    return 0<=x<n and 0<=y<m

directions = [(0,1),(0,-1),(-1,0),(1,0)]

for r in rolling:
    nx,ny = x + directions[r-1][0] , y + directions[r-1][1]
    if is_range(nx,ny):
        x,y = nx,ny
        if r == 1:
            dice.roll_east()
        elif r == 2:
            dice.roll_west()
        elif r == 3:
            dice.roll_north()
        else:
            dice.roll_south()
        if board[x][y] == 0:
            board[x][y] = dice.dice_to_board()
        else:
            dice.board_to_dice(board[x][y])
            board[x][y] = 0
        print(dice.numbers[3])