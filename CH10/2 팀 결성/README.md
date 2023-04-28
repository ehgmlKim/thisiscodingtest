# [CH10] 팀 결성

---
## 문제
### 분류
그래프 이론

### 문제 설명
학교에서 학생들에게 0번부터 N번가지의 번호를 부여했다. 
처음에는 모든 학생이 서로 다른 팀으로 구분되어, 총 N+1개의 팀이 존재한다.
이때 선생님은 '팀 합치기' 연산과 '같은 팀 여부 확인' 연산을 사용할 수 있다.
1. '팀 합치기' 연산은 두 팀을 합치는 연산이다.
2. '같은 팀 여부 확인' 연산은 특정하 두 학생이 같은 팀에 속하는지를 확인하는 연산이다.

선생님이 M개의 연산을 수행할 수 있을 때, '같은 팀 여부 확인' 연산에 대한 연산 결과를 출력하는 프로그램을 작성하시오.

### 입력 조건
- 첫째 줄에 N,M이 주어진다. M은 입력으로 주어지는 연산의 개수이다.(1<=N,M<=100,000)
- 다음 M개의 줄에는 각각의 연산이 주어진다.
- '팀 합치기' 연산은 0 a b 형태로 주어지다. 이는 a번 학생이 속하 팀과 b번 학생이 속한 팀을 합친다는 의미이다.
- '같은 팀 여부 확인' 연산은 1 a b 형태로 주어진다. 이는 a번 학생과 b번 학생이 같은 팀에 속해 있는지를 확인하는 연산이다.
- a와 b는 N이하의 양의 정수이다.

### 출력 조건
- '같은 팀 여부 확인' 연산에 대하여 한 줄에 하나씩 YES 혹은 NO로 결과를 출력한다.

---
## 풀이
```python
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
```
플로이드 위셜 알고리즘으로 풀이했지만, 주어지는 값들의 조건을 보니 시간 초과로 실패할 것 같다.
다익스트라 알고리즘을 이용해서 다시 풀이했다.