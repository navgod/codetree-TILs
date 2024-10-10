k ,n = map(int , input().split())

ans = []

def choose(curridx,lst):
    if curridx == n:
        for i in lst:
            print(i, end= ' ')
        print()
        return
    for i in range(1,k+1):
        lst.append(i)
        choose(curridx+1,lst)
        lst.pop()
choose(0,ans)