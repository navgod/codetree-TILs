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
    for a in selected_line:
        temp[a-1], temp[a] = temp[a], temp[a-1]
    return temp == target

ans = m+1

def min_cnt(cnt,idx):
    global ans
    if cnt == k:
        if check():
            ans = min(ans ,cnt)
        return 

    for i in range(1,n):
        selected_line.append(i)
        min_cnt(cnt+1,i+1)
        selected_line.pop()


for k in range(m+1):
    selected_line = []
    min_cnt(0,0)
print(ans)