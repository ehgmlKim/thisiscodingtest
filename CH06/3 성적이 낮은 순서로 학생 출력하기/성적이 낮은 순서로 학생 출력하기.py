import sys
input = sys.stdin.readline
n = int(input())
#dict = {}
#for _ in range(n):
#    name, score = input().split()
#    dict[name] = int(score)
#dict = sorted(dict.items(), key = lambda x : x[1])
#for k, v in dict:
#    print(k, end=' ')
arr = []
for _ in range(n):
    name, score = input().split()
    arr.append((name, int(score)))
arr = sorted(arr, key=lambda x : x[1])
for a in arr:
    print(a[0], end=' ')