now = input()
row = 'abcdefgh'
x = int(now[1])
y = row.find(now[0])+1
cnt1, cnt2 = 0, 0
# 이동하는 방법 찾기
# 1. 수평으로 2칸 이동한 뒤에 수직으로 1칸 이동하는 경우의 수
if y>2 and y<7:
    cnt1 = 2
else:
    cnt1 = 1
if x>1 and x<8:
    cnt1 *= 2
# 2. 수직으로 2칸 이동한 뒤에 수평으로 1칸 이동하는 경우의 수
if x>3 and x<7:
    cnt2 = 2
else:
    cnt2 =1
if y>1 and y<8:
    cnt2 *= 2
print(cnt1+cnt2)
