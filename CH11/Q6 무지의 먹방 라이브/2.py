from collections import deque


answer = -1
q = deque()
food_times = [1,2,1]
k = 5
for i, t in enumerate(food_times):
    q.append([i + 1, t])

for _ in range(k):
    if not q:
        print(-1)
        break
    d = q.popleft()
    if d[1]:
        d[1] -= 1
        if d[1]:
            q.append(d)
    print(q)
if q:
    d = q.popleft()
    answer = d[0]

print(answer)




