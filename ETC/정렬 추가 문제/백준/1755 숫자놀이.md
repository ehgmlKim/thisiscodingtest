# [Silver IV] 숫자놀이 - 1755 

[문제 링크](https://www.acmicpc.net/problem/1755) 

### 성능 요약

메모리: 31256 KB, 시간: 44 ms

### 분류

수학, 문자열, 정렬

### 문제 설명

<p>79를 영어로 읽되 숫자 단위로 하나씩 읽는다면 "seven nine"이 된다. 80은 마찬가지로 "eight zero"라고 읽는다. 79는 80보다 작지만, 영어로 숫자 하나씩 읽는다면 "eight zero"가 "seven nine"보다 사전순으로 먼저 온다.</p>

<p>문제는 정수 M, N(1 ≤ M ≤ N ≤ 99)이 주어지면 M 이상 N 이하의 정수를 숫자 하나씩 읽었을 때를 기준으로 사전순으로 정렬하여 출력하는 것이다.</p>

### 입력 

 <p>첫째 줄에 M과 N이 주어진다.</p>

### 출력 

 <p>M 이상 N 이하의 정수를 문제 조건에 맞게 정렬하여 한 줄에 10개씩 출력한다.</p>


## ✔️풀이
딕셔너리를 사용해 풀이했다.
먼저, 숫자를 문자로 바꿔줄 `dict`를 만들었다.
`dict`을 이용해 `m`이상 `n`이하의 숫자들을 문자로 바꾸고 `arr_dict`에 `key` 값은 숫자 `value`는 문자열로 넣어줬다. 
이후 문자, 즉 `value`의 값을 기준으로 정렬 후 `key`값을 출력했다.

```python
import sys
input = sys.stdin.readline
dict = {0:'zero ', 1:'one ', 2:'two ', 3:'three ', 4:'four ', 5:'five ', 6:'six ', 7:'seven ', 8:'eight ', 9:'nine '}

m, n = map(int, input().split())
arr_dict = {}

for num in range(m, n+1):
  s = ''
  for i in str(num):
    s += dict[int(i)]
  arr_dict[num] = s
#print(arr_dict)
arr_dict = sorted(arr_dict.items(), key = lambda x:x[1])
#print(arr_dict)
i = 0
for k in arr_dict:
  if i==10:
    i = 0
    print()
  print(k[0], end=' ')
  i += 1
  
```
