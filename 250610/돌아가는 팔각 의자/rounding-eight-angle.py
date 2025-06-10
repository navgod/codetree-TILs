from collections import deque

chairs = [deque(list(map(int,input()))) for _ in range(4)] #12시 부터 시계방향
k = int(input())
commands = [tuple(map(int,input().split())) for _ in range(k)]

def rotate(queue ,dir):
    if dir == -1: # 반시계
        queue.append(queue.popleft())
    else: # 시계
        queue.appendleft(queue.pop())
    return queue

for n , d in commands:
    n = n-1
    candidate = [(n,d)]
    l, r = n-1 , n+1
    # 왼쪽 먼저 전파
    now_n, now_d = n , d
    while 0 <= l and chairs[l][2] != chairs[now_n][6]:
        candidate.append((l,-now_d))
        l , now_n, now_d = l-1, now_n-1, -now_d 
    now_n, now_d = n , d
    while r<4 and chairs[now_n][2] != chairs[r][6]:
        candidate.append((r,-now_d))
        r, now_n, now_d = r+1 , now_n +1 , -now_d
    for now_n , now_d in candidate:
        chairs[now_n] = rotate(chairs[now_n],now_d)
    

print(sum([chairs[i][0]*2**i for i in range(4)]))