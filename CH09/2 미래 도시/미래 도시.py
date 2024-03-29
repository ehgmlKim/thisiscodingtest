# 플로이드 워셜 알고리즘으로 풀이
import sys
imput = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
graph = [ [INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    graph[a][a] = 0

# 각 간선에 대한 정보를 입력받아 그 값으로 초기화
for _ in range(m):
    x,k = map(int, input().split())
    graph[x][k] = 1
    graph[k][x] = 1

#X와 K
X, K = map(int, input().split())
# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

d = graph[1][k] + graph[k][x]
if d >= INF:
    print(-1)
else:
    print(d)