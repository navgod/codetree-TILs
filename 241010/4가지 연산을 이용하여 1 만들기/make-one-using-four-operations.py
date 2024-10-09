from collections import deque
n = int(input())

visited = [0]*(n+2)
step = [0]*(n+2)

q = deque()
q.append(n)
visited[n] = 1

def is_range(x):
    return 0<x<=n+1
def can_go(x):
    return is_range(x) and not visited[x]
def push(x,s):
    visited[x] = 1
    step[x] = s
    q.append(x)
def bfs():
    while q:
        x = q.popleft()
        if x == 1:
            print(step[x])
            return
        if can_go(x-1):
            push(x-1,step[x]+1)
        if can_go(x+1):
            push(x+1,step[x]+1)
        if x%2 == 0 and can_go(x//2):
            push(x//2,step[x]+1)
        if x%3 == 0 and can_go(x//3):
            push(x//3,step[x]+1)
bfs()