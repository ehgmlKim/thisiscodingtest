import sys
input = sys.stdin.readline
n = int(input())
have = list(map(int, input().split()))
m = int(input())
want = list(map(int, input().split()))

#시간 초과나는 풀이
#for w in want:
#    if w in have:
#        print('yes', end=' ')
#    else:
#        print('no', end=' ')
def find_one(start, end, target, have):
    if start>end:
        print('no', end=' ')
        return
    mid = (start+end)//2
    if have[mid] == target:
        print('yes', end=' ')
        return
    elif have[mid]>target:
        find_one(start, mid - 1, target, have)
    else:
        find_one(mid+1, end, target, have)
have = sorted(have)
for i in range(m):
    find_one(0, n, want[i], have)