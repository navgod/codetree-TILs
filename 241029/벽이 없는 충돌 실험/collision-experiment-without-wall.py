from collections import deque

def move():
    for _ in range(len(beads)):
        bead = beads.popleft()
        x,y,w,d = bead
        dx,dy = dxs[d], dys[d]
        beads.append([x+dx*0.5,y+dy*0.5,w,d])

def check(t):
    global last
    unique_coord = set()
    duplicated_coord = set()
    new_beads = deque()
    crash_idx = dict()
    for idx,bead in enumerate(beads):
        x,y,w,d = bead
        if (x,y) in unique_coord:
            duplicated_coord.add((x,y))
        else:
            unique_coord.add((x,y))
    for idx, bead in enumerate(beads):
        x, y, w, d = bead
        if (x, y) in duplicated_coord:
            if (x, y) in crash_idx:
                crash_idx[(x, y)].append(idx)
            else:
                crash_idx[(x, y)] = [idx]
        else:
            new_beads.append(beads[idx])
    for key, val in crash_idx.items():
        target = [(beads[idx][2], idx) for idx in val]
        winner = sorted(target, key=lambda x: (x[0], x[1]), reverse=True)[0]
        new_beads.append(beads[winner[1]])
        last = t

    return new_beads

T = int(input())

dir_map = {
    'U':0,
    'D':1,
    'R':2,
    'L':3
}

dxs , dys = [0,0,1,-1] , [1,-1,0,0]

for _ in range(T):
    n= int(input())
    # x y w d
    beads = deque()
    for _ in range(n):
        x,y,w,d = input().split()
        beads.append([int(x),int(y),int(w),dir_map[d]])
    last = -1
    for time in range(1,4004):
        move()
        new_beads = check(time)
        beads = new_beads
    print(last)