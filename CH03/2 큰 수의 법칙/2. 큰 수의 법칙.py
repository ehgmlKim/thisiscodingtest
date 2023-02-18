N, M, K = map(int, input().split())
arr=list(map(int, input().split()))
## 내림차순으로 정렬하기
sort_arr = sorted(arr, reverse = True)
## M에 연속한 K번이 들어갈 수 있는만큼 가장 큰 수를 더해주고
## 연속한 K번이 들어가고 남은 자리만큼 두번째로 큰 수를 더해준다.
print(sort_arr[0]*(M//K)*K+sort_arr[1]*(M%K) )
