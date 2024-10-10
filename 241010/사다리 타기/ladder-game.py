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

selected_line = []

def check():
    temp = [i for i in range(1,n+1)]
    for a in selected_line:
        temp[a-1], temp[a] = temp[a], temp[a-1]
    return temp == target

ans = m+1

def min_cnt(cnt,maxi):
    global ans
    if check():
        ans = min(ans ,cnt)
        return 
    if cnt >maxi:
        return 
    if maxi > m:
        ans = m
        return
    for i in range(1,n):
        selected_line.append(i)
        min_cnt(cnt+1,maxi)
        selected_line.pop()
maxi = 1
while ans == m+1:
    min_cnt(0,maxi)
    maxi +=1
print(ans)