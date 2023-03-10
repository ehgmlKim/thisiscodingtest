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
for a in arr:
    print(a)
