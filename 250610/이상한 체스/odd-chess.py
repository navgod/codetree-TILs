from copy import deepcopy

# 방향: 북, 동, 남, 서 (문제 세팅에 따라 달라질 수 있음)
dirs = [(-1,0), (0,1), (1,0), (0,-1)] 

# 각 cctv별 방향 조합 정의 (문제에서 주어진대로 직접 하드코딩)
cctv_dirs = [
    [],  # 0번 없음
    [[0], [1], [2], [3]],                           # 1번
    [[0,2], [1,3]],                                 # 2번
    [[0,1], [1,2], [2,3], [3,0]],                   # 3번
    [[0,1,2], [1,2,3], [2,3,0], [3,0,1]],           # 4번
    [[0,1,2,3]],                                    # 5번
]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

cctvs = []
for i in range(n):
    for j in range(m):
        if 1 <= board[i][j] <= 5:
            cctvs.append((i, j, board[i][j]))

result = n * m

def fill(tmp, r, c, directions):
    for d in directions:
        nr, nc = r, c
        while True:
            nr += dirs[d][0]
            nc += dirs[d][1]
            if not (0 <= nr < n and 0 <= nc < m):
                break
            if tmp[nr][nc] == 6:   # 벽 만나면 중단
                break
            if tmp[nr][nc] == 0:   # 감시할 수 있으면 표시
                tmp[nr][nc] = '#'

def dfs(depth, tmp):
    global result
    if depth == len(cctvs):
        cnt = sum(row.count(0) for row in tmp)
        result = min(result, cnt)
        return
    x, y, cctv_type = cctvs[depth]
    for dirs_case in cctv_dirs[cctv_type]:
        nxt = deepcopy(tmp)
        fill(nxt, x, y, dirs_case)
        dfs(depth+1, nxt)

dfs(0, board)
print(result)