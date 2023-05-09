import sys
input = sys.stdin.readline

S = input().rstrip()
al = ''
sum = 0
for s in S:
    if s.isalpha():
        al += s
    else:
        sum += int(s)

al = sorted(al)
print(''.join(al) + str(sum))
