import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
indegree = [0] * (n+1)
graph = [[] for i in range(n+1)]
time = [[] for i in range(n+1)]
for i in range(1, n+1):
    arr = list(map(int, input().split()))
    time[i] = arr[0]
    for j in range(1, len(arr)-1):
        graph[arr[j]].append(i)
        indegree[i] += 1

result = time

for i in range(1, n+1):
    for a in graph[i]:
        result[a] += time[i]

for i in range(1, n+1):
    print(result[i])