# [CH04] 게임 개발

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

---
## 풀이
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
