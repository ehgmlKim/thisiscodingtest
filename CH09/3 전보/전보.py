import sys
input = sys.stdin.readline
INF = int(1e9)

# N 도시의 개수 M 통로의 개수 C 메시지를 보내고자하는 도시
N,M,C = map(int, input().split())

graph = [[] for i in range(N+1)]

for _ in range(M):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))

#print(graph)
city = {x[0] : x[1] for x in graph[C]}
#print(city)

for i in range(1, N+1):
    if i in city:
        for node, dis in graph[i]:
            if node in city: #이미 있을 때, 한번에 가는 방법보다 다른데를 거쳐서 가는게 더 빠르면 그걸로 바꾼다
                if city[node] > city[i] + dis:
                    city[node] = city[i]+dis
            else:
                city[node] = dis
#print(city)
city_time = [x[1] for x in city.items()]

print(len(city), max(city_time))