import sys
input = sys.stdin.readline

n, m= map(int, input().split())
arr = list(map(int, input().split()))

dict={}

for a in arr:
    if a in dict:
        dict[a] += 1
    else:
        dict[a] = 1
result = 0
dict = list(dict.items())
for i in range(len(dict)-1):
    for j in range(i+1, len(dict)):
        result += dict[i][1] * dict[j][1]
print(result)