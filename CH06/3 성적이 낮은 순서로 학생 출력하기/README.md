# [CH06] 성적이 낮은 순서로 학생 출력하기

---
## 문제
### 분류
정렬

### 문제 설명
N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다.
각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.

### 입력 조건
- 첫째 줄에 학생의 수 N이 입력된다. (1 <= N <= 100,000)
- 둘째 줄부터 N+1번째 줄에는 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가
공백으로 구분되어 입력된다. 문자열 A의 길이와 학생의 성적은 100 이하의 자연수이다.

### 출력 조건
- 모든 학생의 이름을 성적이 낮은 순서대로 출력한다. 성적이 동일한 학생들의 순서는 자유롭게 출력해도
괜찮다.

---
## 풀이
### 딕셔너리를 이용한 풀이
```python
import sys
input = sys.stdin.readline
n = int(input())
dict = {}
for _ in range(n):
    name, score = input().split()
    dict[name] = int(score)
dict = sorted(dict.items(), key = lambda x : x[1])
for k, v in dict:
    print(k, end=' ')
```
입력받은 이름:성적 으로 딕셔너리를 만든다.
성적을 기준으로 딕셔너리를 정렬하고, key값인 이름을 한줄로 출력한다.<br>
다만, 문제에서 학생 정보는 이름과 성적으로 구분된다고 했으므로 동명이인이 있을 경우,
이름이 key 값인 위의 딕셔너리는 오류가 생길 수 있다. 따라서 튜플을 이용한 풀이로 수정했다.

### 튜플을 이용한 풀이
```python
import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    name, score = input().split()
    arr.append((name, int(score)))
arr = sorted(arr, key=lambda x : x[1])
for a in arr:
    print(a[0], end=' ')
```