n, m = map(int, input().split())

arr = [] #미로
for _ in range(n):
    arr.append(list(map(int, input())))
dd = [[-1, 0], [1, 0], [0, -1], [0, 1]] #상하좌우

def bfs(x, y, arr):
    for dx, dy in dd:
        nx = x + dx
        ny = y + dy
        if x==n-1 and y==m-1:
            return
        if 0 <= nx < n and 0 <= ny < m:  # 범위 안일 때
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                bfs(nx, ny,arr)
bfs(0,0,arr)
for a in arr:
    print(a)
print(arr[n-1][m-1])