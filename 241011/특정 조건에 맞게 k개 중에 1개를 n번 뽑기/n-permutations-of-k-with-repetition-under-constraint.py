k, n = map(int , input().split())

ans = []

def choose(idx):
    if idx == n:
        for i in ans:
            print(i, end= ' ')
        print()
        return

    for i in range(1,k+1):
        if not ans:
            ans.append(i)
            choose(idx+1)
            ans.pop()
        elif i == ans[-1]:
            if len(ans) <2:
                ans.append(i)
                choose(idx+1)
                ans.pop()
            elif i != ans[-2]:
                ans.append(i)
                choose(idx+1)
                ans.pop()
        else:
            ans.append(i)
            choose(idx+1)
            ans.pop()

choose(0)