import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()


def binary(start, end, m):
    mid = (start + end) // 2
    h = [t - mid for t in arr if t > mid]
    if (start > end):
        return end
    if sum(h) >= m:
        return binary(mid + 1, end, m)
    else:
        return binary(start, mid - 1, m)


print(binary(1, arr[-1], m))