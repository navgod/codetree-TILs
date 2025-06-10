n , L = map(int, input().split())
height = [list(map(int, input().split())) for _ in range(n)]

def check_arr(arr):
    keep_num, cnt = None, 0
    for i in range(n):
        now = arr[i]
        if i == 0 :
            keep_num, cnt = now , 1
            continue
        if now == keep_num:
            cnt +=1
        else:
            if abs(now - keep_num) > 1 or cnt <0:
                return 0
            if now > keep_num:
                if cnt >= L:
                    keep_num, cnt = now ,1
                else:
                    return 0
            else:
                keep_num, cnt = now , -L+1
    return 0 if cnt <0 else 1
ans = 0
for i in range(n):
    ans += check_arr(height[i])
for i in range(n):
    ans += check_arr([height[j][i] for j in range(n)])

print(ans)