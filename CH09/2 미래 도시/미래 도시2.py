import sys
imput = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
graph = {}

# 각 간선에 대한 정보를 입력받아 그 값으로 초기화
for _ in range(m):
    x,k = map(int, input().split())
    if x in graph:
        graph[x].append(k)
    else:
        graph[x] = [k]
    if k in graph:
        graph[k].append(x)
    else:
        graph[k] = [x]

#X와 K
X, K = map(int, input().split())
arr = graph[1]
l = len(arr)
distance = 0
def find(arr, F):
    if F in arr:
        return 1
    else:
        return 0
while True:
    if K in arr:
        distance += 1
    else:
        for a in arr:
            if K in graph[a]:
                distance += 1