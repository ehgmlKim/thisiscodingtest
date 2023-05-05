import sys
input = sys.stdin.readline

n = int(input())
arr=list(map(int, input().split()))
team = [[] for i in range(n)]

arr.sort()
i = 0
while arr:
    x = arr[-1]
    team[i].append(x)
    arr.remove(x)
    for j in range(x-1):
        x = arr[-1]
        team[i].append(x)
        arr.remove(x)
    i += 1
count = 0
for t in team:
    if t:
        count += 1
print(count)