# [CH05] 미로 탈출

## 문제
### 분류

DFS/BFS

### 문제 설명
동빈이는 N X M 크기의 직사각형 형태의 미로에 갇혀 있다.
미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다.
동빈이의 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한번에 한 칸씩 이동할 수 있다.
이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다.
미로는 반드시 탈출할 수 있는 형태로 제시된다. 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오.
칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

### 입력 조건
- 첫째 줄에 두 정수 N, M(4<=N, M<=200)이 주어집니다. 다음 N개의 줄에는 각각 M개의 정수(0 ghrdms 1)로 미로의 정보가 주어진다.
각각의 수들은 공백 없이 붙어서 입력으로 제시된다. 또한 시작 칸과 마지막 칸은 항상 1이다.

### 출력 조건
- 첫째 줄에 최소 이동 칸의 개수를 출력한다.

## 풀이
### 예제만 맞은 풀이
```python
n, m = map(int, input().split())

arr = [] #미로
for _ in range(n):
    arr.append(list(map(int, input())))
dd = [[-1, 0], [1, 0], [0, -1], [0, 1]] #상하좌우


visited = [[0]*m for _ in range(n)]
visited[0][0] = 1

for x in range(n):
    for y in range(m):
        if arr[x][y] == 0:
            pass
        else:
            for dx, dy in dd:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m:  # 범위 안일 때
                    if not visited[nx][ny] and arr[nx][ny] == 1:
                        arr[nx][ny] = arr[x][y] + 1
                        visited[nx][ny] = 1
#for a in arr:
#    print(a)
print(arr[n-1][m-1])
```
1. 현재 위치에서 상하좌우를 확인한다.
2. 미로 범위 내에서 방문하지 않았고, 괴물이 없다면 이동하기 전 배열의 값(해당 배열까지 움직인 칸의 개수)에 1을 더한 값을 대입한다.
3. 이동한 위치를 방문했다고 표시해준다.

해당 코드는 오른쪽 아래로만 이동하는 미로의 경우 정답을 출력한다.
하지만 더 이상 길이 없어 다시 돌아와야 하는 경우, 이미 방문한 위치를 제외하기 때문에 그 부분이 빼고 계산된다.

### 교제 답안 예시
```python
from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의 (상, 하, 좌, 우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# bfs 소스코드 구현
def bfs(x, y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    # 큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간 범위를 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 괴물이 있는 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

# bfs를 수행한 결과 출력
print(bfs(0,0))
```
