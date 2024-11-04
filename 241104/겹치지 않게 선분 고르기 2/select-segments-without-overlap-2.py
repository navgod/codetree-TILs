n = int(input())

lines = [list(map(int , input().split())) for _ in range(n)]

lines.sort(key = lambda x: x[1])

ans = 0
while lines:
    ans +=1
    x1, x2 = lines[0]
    new_line = []
    for xx1,xx2 in lines:
        if xx1 > x2:
            new_line.append([xx1,xx2])
    lines = new_line

print(ans)