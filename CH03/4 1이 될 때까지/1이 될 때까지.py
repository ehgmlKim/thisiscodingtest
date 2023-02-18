n, k = map(int, input().split())
count = 0
while n>1:
  # n이 k로 나누어 떨어지면 나누어주고
  if n%k==0:
    n //= k
  # n이 k로 나누어 떨어지지 않으면 -1
  else:
    n -= 1
  count += 1
print(count)
