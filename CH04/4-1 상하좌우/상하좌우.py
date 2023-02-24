n = int(input())
move = input().split()
x, y = 1, 1
for m in move:
    if 1 < y and m == "L":
        y -= 1
    if 1 < x and m == "U":
        x -= 1
    if y < n and m == "R":
        y += 1
    if x < n and m == "D":
        x += 1
    #print(m, x, y)
print(x, y)
