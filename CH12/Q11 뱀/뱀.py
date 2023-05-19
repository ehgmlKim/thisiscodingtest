import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [[0]*n for _ in range(n)]
board[0][0] = 1
#print(board)
K = int(input())
for _ in range(K):
    x,y = map(int, input().split())
    board[x][y] = 1 #사과의 위치
L = int(input())
times = {}
for _ in range(L):
    x, C =input().split()
    times[int(x)] = C
#뱀의 현재 위치
x = 0
y = 0
time = 0
snake = deque([(0,0)])
dx = [1,0,-1,0]
dy = [0,1,0,-1]
i=0
while True:
    nx, ny = x+dx[i], y+dy[i]
    if nx<0 or ny<0 or nx>n-1 or ny>n-1 or (nx, ny) in snake:
        break
    if not board[ny][nx]: #사과가 없으면 꼬리 없애기
        a, b = snake.popleft()
        board[b][a] = 0
    x, y = nx, ny
    board[y][x] = 1
    snake.append((nx, ny))
    time += 1

    if time in times.keys():
        if times[time] == 'D':
            i = (i+1)%4
        else:
            ni = 3 if i==0 else i-1
            i = ni
print(time+1)