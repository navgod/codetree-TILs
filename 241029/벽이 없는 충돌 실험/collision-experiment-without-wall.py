def move():
    for idx, bead in enumerate(beads):
        x,y,w,d = bead
        dx, dy = dxs[d], dys[d]
        beads[idx] = [x+dx*0.5,y+dy*0.5,w,d]

def check(t):
    global last
    crash_idx = dict()
    new_beads = []
    for idx,bead in enumerate(beads):
        x,y,w,d = bead
        if (x,y) in crash_idx:
            crash_idx[(x,y)].append(idx)
        else:
            crash_idx[(x,y)] = [idx]
    for key, val in crash_idx.items():
        if len(val)>1:
            target = [(beads[idx][2],idx) for idx in val]
            winner = sorted(target, key= lambda x: (x[0],x[1]), reverse = True)[0]
            new_beads.append(beads[winner[1]])
            last = t
        else:
            new_beads.append(beads[val[0]])
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
    beads = [ [int(x[0]), int(x[1]), int(x[2]), dir_map[x[3]]]  for x in (input().split() for _ in range(n))]
    last = -1
    for time in range(1,4004):
        move()
        new_beads = check(time)
        beads = new_beads
    print(last)