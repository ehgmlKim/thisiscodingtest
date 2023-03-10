# [CH04] 게임 개발

## 문제
>
### 분류
DFS/BFS
>
### 문제 설명
N X M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.
>
### 입력 조건
- 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다. (1 <= N, M <= 1,000)
- 두 번째 줄부터 N + 1번째 줄까지 얼음 틀의 형태가 주어진다.
- 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.
>
### 출력 조건
- 한 번에 만들 수 있는 아이스크림의 개수를 출력한다.

## 풀이
### 교재 답안 예시
```python
def dfs(arr, x, y, visited):
    dd = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    visited[x][y] = True

    for dx, dy in dd:
        nx = x + dx
        ny = y + dy
        if 0<=nx<n and 0<=ny<m : # 움직였을 때 범위 안
            x = nx
            y = ny
            if not visited[x][y] and arr[x][y] == 0:
                dfs(arr, x, y, visited)


n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input())))
visited = [[False]*m for _ in range(n)]
answer = 0

for i in range(n):
  for j in range(m):
    # 아직 방문하지 않은 구멍 뚫린 부분인 경우만
    if not visited[i][j] and arr[i][j] == 0:
      answer += 1
      dfs(arr, i, j, visited)
print(answer)
```
