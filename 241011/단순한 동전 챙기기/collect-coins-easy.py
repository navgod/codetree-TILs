n = int(input())

grid = [list(input()) for _ in range(n)]

nums = []
for x in range(n):
    for y in range(n):
        if grid[y][x].isdigit():
            nums.append((int(grid[y][x]),x,y))
        elif grid[y][x] =='S':
            start =(x,y)
        elif grid[y][x] == 'E':
            end = (x,y)
if len(nums)>= 3:
    possible = True
else:
    possible = False

nums.sort()

ans = 3*n**2+1

selected_num = []

def move(idx):
    global ans
    if not possible:
        return
    if idx == len(nums):
        if len(selected_num) >=4 :
            val = 0
            selected_num.append(end)
            last_x, last_y = None , None
            for x,y in selected_num:
                if last_x != None:
                    val += abs(last_x-x)+abs(last_y-y)
                last_x, last_y = x,y
            selected_num.pop()
            ans = min(ans ,val)
        return
    selected_num.append((nums[idx][1],nums[idx][2]))
    move(idx+1)
    selected_num.pop()
    move(idx+1)

selected_num.append(start)

move(0)


if not possible or ans > 3*n**2:
    ans = -1

print(ans)