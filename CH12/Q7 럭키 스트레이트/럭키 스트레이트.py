import sys
input = sys.stdin.readline

n = input().rstrip()
l = len(n)//2
front = n[:l]
back = n[l:]
sum = 0
for f in front:
    sum += int(f)
for b in back:
    sum -= int(b)
if sum:
    print("READY")
else:
    print("LUCKY")
