import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
# 1 2 3 4 5
for i in range(n):
    if i == 2:
        arr[i] += arr[i-2]
    if i>2:
        arr[i] += max(arr[i-2], arr[i-3])
    #print(arr)
print(max(arr[-1], arr[-2]))