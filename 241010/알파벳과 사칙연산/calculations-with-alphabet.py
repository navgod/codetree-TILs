from collections import deque
import sys
target = input()

selected = []

ans = -sys.maxsize

def calc():
    val = selected[ord(target[0])-97]
    for i in range(1,len(target),2):
        if target[i] == '*':
            val *= selected[ord(target[i+1])-97]
        elif target[i] == '-':
            val -= selected[ord(target[i+1])-97]
        elif target[i] == '+':
            val += selected[ord(target[i+1])-97]
    return val

def simul(cnt):
    global ans

    if cnt == 6:
        ans = max(ans,calc())
        return
    for i in range(1,5):
        selected.append(i)
        simul(cnt+1)
        selected.pop()
    
simul(0)
print(ans)