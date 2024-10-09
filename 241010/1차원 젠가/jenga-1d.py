n = int(input())
block = []
for _ in range(n):
    block.append(int(input()))
s1, e1 = map(int , input().split())
temp = []
for i in range(s1-1):
    temp.append(block[i])
for i in range(e1,n):
    temp.append(block[i])
s2, e2 = map(int , input().split())
block = temp
temp = []
for i in range(s2-1):
    temp.append(block[i])
for i in range(e2,len(block)):
    temp.append(block[i])
print(len(temp))
for i in temp:
    print(i)