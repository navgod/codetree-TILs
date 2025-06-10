n = int(input())
nums = list(map(int,input().split()))
oper_cnt = list(map(int,input().split()))
operator = []

my_min = float('inf')
my_max = -float('inf')

int_to_oper = {
    0 : '+',
    1 : '-',
    2 : '*'
}

def cal_nums():
    temp = []
    for i in range(2*n-1):
        if i%2 == 0:
            temp.append(nums[i//2])
        else:
            temp.append(operator[i//2])
    keep_num,keep_oper = None , None
    ans = 0
    for c in temp:
        if type(c) == type(1): #숫자일때
            if keep_oper:
                if keep_oper == '*':
                    ans *= c
                elif keep_oper == '+':
                    ans += c
                else:
                    ans -= c
            else:
                ans = c
        else: #문자일 때
            keep_oper = c
    return ans

def dfs(depth):
    if depth == n-1:
        global my_max, my_min
        now = cal_nums()
        my_max = max(my_max, now)
        my_min = min(my_min, now)
        return
    for i in range(3):
        if oper_cnt[i] >0:
            oper_cnt[i] -=1
            operator.append(int_to_oper[i])
            dfs(depth+1)
            operator.pop()
            oper_cnt[i] +=1
dfs(0)

print(my_min, my_max)