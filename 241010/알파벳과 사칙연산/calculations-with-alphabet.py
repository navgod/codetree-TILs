from collections import deque
import sys
target = input()

selected = []

ans = -sys.maxsize

def calc():
    val = selected[0]
    for i in range(1,len(target),2):
        if selected[i] == '*':
            val *= selected[i+1]
        elif selected[i] == '-':
            val -= selected[i+1]
        elif selected[i] == '+':
            val += selected[i+1]
    return val

def simul(idx):
    global ans

    if idx == len(target):
        ans = max(ans,calc())
        return

    if idx %2 ==0:
        for i in range(1,5):
            selected.append(i)
            simul(idx+1)
            selected.pop()
    else:
        selected.append(target[idx])
        simul(idx+1)
        selected.pop()

simul(0)
print(ans)