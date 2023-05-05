import sys
input = sys.stdin.readline

S = input().rstrip()
count = 1
for i in range(1, len(S)):
    if S[i-1] != S[i]:
        count+=1

print(count//2)