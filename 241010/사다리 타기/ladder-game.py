import copy
n, m = map(int , input().split())

lines = [list(map(int , input().split())) for _ in range(m)]
now = [i for i in range(1,n+1)]
sorted_lines = sorted(lines, key = lambda x: x[1])

def shift(a):
    now[a-1] , now[a] = now[a] , now[a-1]

for a, b in sorted_lines:
    shift(a)

target = copy.deepcopy(now)

def check():
    temp = [i for i in range(1,n+1)]

    for a, b in selected_lines:
        temp[a-1], temp[a] = temp[a], temp[a-1]

    return temp == target

ans = m

def min_cnt(idx):
    global ans

    if idx == m:
        if check():
            ans = min(ans ,len(selected_lines))
        return 
    selected_lines.append(sorted_lines[idx])
    min_cnt(idx +1 )
    selected_lines.pop()
    min_cnt(idx+ 1 )

selected_lines= []

min_cnt(0)

print(ans)