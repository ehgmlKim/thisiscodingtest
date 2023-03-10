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
