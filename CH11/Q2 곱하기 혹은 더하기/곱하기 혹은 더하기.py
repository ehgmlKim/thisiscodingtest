import sys
input = sys.stdin.readline

S = input().rstrip()
result = 0

for s in S:
    if s == '0' or s == '1':
        result += int(s)
    if result == 0:
        result += int(s)
    else:
        result *= int(s)

print(result)