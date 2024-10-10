n = int(input())

lines = [list(map(int, input().split())) for _ in range(n)]

selected_lines = []

ans = 0

def is_overlap(s,e):
    for x1, x2 in selected_lines:
        if s <= x1 <= e or s <= x2 <= e or (x1<= s and e <=x2):
            return True
    return False

def find_max(idx, cnt):
    global ans

    if idx == len(lines):
        ans = max(ans, cnt)
        return
    
    s,e = lines[idx]

    if not is_overlap(s,e):
        selected_lines.append((s,e))
        find_max(idx+1,cnt+1)
        selected_lines.pop()
    find_max(idx+1,cnt)
find_max(0,0)

print(ans)