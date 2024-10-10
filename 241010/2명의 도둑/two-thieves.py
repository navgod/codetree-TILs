n, m , c = map(int , input().split())
rooms = [list(map(int , input().split())) for _ in range(n)]

# (행, 시작열, 끝 열) 형태
selected_room = []

selected_goods = []

ans = 0

def optimize(idx,thief):
    global tmp_val
    val = 0
    if idx == len(thief):
        for i in selected_goods:
            val += i **2
        tmp_val = max(tmp_val, val)
        return
    if not (sum(selected_goods)+thief[idx] >c):
        selected_goods.append(thief[idx])
        optimize(idx+1,thief)
        selected_goods.pop()
    optimize(idx+1,thief)

def max_cal(thief):
    val = 0
    if sum(thief) <= c:
        for i in thief:
            val += i**2
    else:
        global tmp_val
        tmp_val = 0
        optimize(0,thief)
        val += tmp_val
    return val

def calc():
    val = 0
    thief1 = []
    thief2 = []

    row1 , sc1, ec1 = selected_room[0]
    row2 , sc2, ec2 = selected_room[1]
    for i in range(sc1,ec1+1):
        thief1.append(rooms[row1][i])
    for i in range(sc2,ec2+1):
        thief2.append(rooms[row2][i])
    val = max_cal(thief1) + max_cal(thief2)
    return val

def overlap(row2,sc2,ec2):
    if not selected_room:
        return False
    row1, sc1,ec1 = selected_room[0]
    if row1 != row2:
        return False
    if sc1<= sc2 <= ec1 or sc1<= ec2 <= ec1 or (sc2<= sc1 <=ec2):
        return True
    return False

def find_max_val(num):
    global ans
    if num ==2:
        if len(selected_room) ==2:
            ans = max(ans, calc())
        return
    for row in range(n):
        for col in range(n-m+1):
            if not overlap(row,col, col+m-1):
                selected_room.append((row,col,col+m-1))
                find_max_val(num+1)
                selected_room.pop()

find_max_val(0)
print(ans)