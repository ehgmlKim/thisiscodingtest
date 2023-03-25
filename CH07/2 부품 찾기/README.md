# [CH07] 부품 찾기
## 문제

### 분류
이진 탐색

### 문제 설명
하나의 수열에는 다양한 수가 존재한다. 이러한 수는 크기에 상관없이 나열되어 있다.
이 수를 큰 수부터 작은 수의 순서로 정렬해야 한다.
수열을 내림차순으로 정렬하는 프로그램을 만드시오.

### 입력 조건
- 첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다. (1 <= N <= 500)
- 둘째 줄부터 N+1번째 줄까지 N개의 수가 입력된다. 수의 범위는
1 이상 100,000 이하의 자연수이다.

### 출력 조건
- 입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력한다.
동일한 수의 순서는 자유롭게 출력해도 괜찮다.

## 풀이
```python
import sys
input = sys.stdin.readline
n = int(input())
have = list(map(int, input().split()))
m = int(input())
want = list(map(int, input().split()))

#시간 초과나는 풀이
#for w in want:
#    if w in have:
#        print('yes', end=' ')
#    else:
#        print('no', end=' ')
def find_one(start, end, target, have):
    if start>end:
        print('no', end=' ')
        return
    mid = (start+end)//2
    if have[mid] == target:
        print('yes', end=' ')
        return
    elif have[mid]>target:
        find_one(start, mid - 1, target, have)
    else:
        find_one(mid+1, end, target, have)
have = sorted(have)

for i in range(m):
    find_one(0, n, want[i], have)
```
