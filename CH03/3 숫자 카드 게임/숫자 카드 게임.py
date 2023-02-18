n,m = map(int, input().split())
min_arr = []
for i in range(n):
  arr=list((map(int, input().split())))
  ## 입력받은 행에서 가장 작은 값을 min_arr에 추가한다.
  min_arr.append(min(arr))

## min_arr에 추가된 값등 중에서 가장 큰 수를 반환한다.
print(max(min_arr))
