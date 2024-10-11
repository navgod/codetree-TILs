n,m = map(int , input().split())

selected_num = []
ans = set()
def choose(idx):
    if idx == m:
        ans.add(tuple(sorted(selected_num)))
        return
    
    for i in range(1,n+1):
        if i not in selected_num:
            selected_num.append(i)
            choose(idx+1)
            selected_num.pop()
    
choose(0)
for a in ans:
    for i in a:
        print(i, end=' ')
    print()