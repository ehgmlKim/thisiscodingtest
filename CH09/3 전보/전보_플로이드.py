# 플로이드 워셜 알고리즘으로 풀이
import sys
input = sys.stdin.readline
INF = int(1e9)

# N 도시의 개수 M 통로의 개수 C 메시지를 보내고자하는 도시
N,M,C = map(int, input().split())

graph = [[INF]*(N+1) for i in range(N+1)]

for _ in range(M):
    x,y,z = map(int, input().split())
    graph[x][y] = z

for i in range(1,N+1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if graph[j][k] > graph[j][i] + graph[i][k]:
                graph[j][k] = graph[j][i] + graph[i][k]

#print(graph)

city_time = [x for x in graph[C] if x < INF]
l = len(city_time)
if l:
    time = max(city_time)
else: #전달할 수 있는 도시가 하나도 없을 경우에 대한 출력예시가 없어서 -1로 출력되도록 함
    time = -1

print(l, time)