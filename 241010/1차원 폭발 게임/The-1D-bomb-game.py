n,m = map(int, input().split())
bomb = []
for _ in range(n):
    bmb = int(input())
    bomb.append(bmb)

def switch():
    global will_explode
    last = 0
    will_explode = []
    tmp = []
    for i in range(len(bomb)):
        if bomb[i] == last:
            tmp.append(i)
        else:
            if len(tmp) >= m:
                will_explode.append(tmp)
            tmp = [i]
            last = bomb[i]
    if tmp and len(tmp) >=m:
        will_explode.append(tmp)

def explode():
    global will_explode, bomb
    if will_explode:
        for i in will_explode:
            for j in i:
                bomb[j] = 0
        temp = []
        for i in bomb:
            if i:
                temp.append(i)
        bomb= temp
last= bomb
switch()
explode()
while last != bomb:
    last = bomb
    switch()
    explode()
if bomb:
    for i in bomb:
        print(i)
else:
    print(0)