# [level 4] 무지의 먹방 라이브 - 42891 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42891#qna) 

### 성능 요약

메모리: 47.9 MB, 시간: 218.37 ms

### 구분

코딩테스트 연습 > 2019 KAKAO BLIND RECRUITMENT

### 채점결과

Empty

### 문제 설명

<h2>무지의 먹방 라이브</h2>

<p><code>* 효율성 테스트에 부분 점수가 있는 문제입니다.</code></p>

<p>평소 식욕이 왕성한 무지는 자신의 재능을 뽐내고 싶어 졌고 고민 끝에 카카오 TV 라이브로 방송을 하기로 마음먹었다.</p>

<p><img src="https://grepp-programmers.s3.amazonaws.com/files/production/10f4f72c93/1d932bfc-8082-4b7e-b30d-ab46bf71a9f2.png" title="" alt="muji_live.png"></p>

<p>그냥 먹방을 하면 다른 방송과 차별성이 없기 때문에 무지는 아래와 같이 독특한 방식을 생각해냈다. </p>

<p>회전판에 먹어야 할 N 개의 음식이 있다. <br>
각 음식에는 1부터 N 까지 번호가 붙어있으며, 각 음식을 섭취하는데 일정 시간이 소요된다. <br>
무지는 다음과 같은 방법으로 음식을 섭취한다.</p>

<ul>
<li>무지는 1번 음식부터 먹기 시작하며, 회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 가져다 놓는다.</li>
<li>마지막 번호의 음식을 섭취한 후에는 회전판에 의해 다시 1번 음식이 무지 앞으로 온다.</li>
<li>무지는 음식 하나를 1초 동안 섭취한 후 남은 음식은 그대로 두고, 다음 음식을 섭취한다.

<ul>
<li>다음 음식이란, 아직 남은 음식 중 다음으로 섭취해야 할 가장 가까운 번호의 음식을 말한다.</li>
</ul></li>
<li>회전판이 다음 음식을 무지 앞으로 가져오는데 걸리는 시간은 없다고 가정한다.</li>
</ul>

<p>무지가 먹방을 시작한 지 K 초 후에 네트워크 장애로 인해 방송이 잠시 중단되었다.<br>
무지는 네트워크 정상화 후 다시 방송을 이어갈 때, 몇 번 음식부터 섭취해야 하는지를 알고자 한다. <br>
각 음식을 모두 먹는데 필요한 시간이 담겨있는 배열 food_times, 네트워크 장애가 발생한 시간 K 초가 매개변수로 주어질 때 몇 번 음식부터 다시 섭취하면 되는지 return 하도록 solution 함수를 완성하라.</p>

<h5>제한사항</h5>

<ul>
<li>food_times 는 각 음식을 모두 먹는데 필요한 시간이 음식의 번호 순서대로 들어있는 배열이다.</li>
<li>k 는 방송이 중단된 시간을 나타낸다.</li>
<li>만약 더 섭취해야 할 음식이 없다면 <code>-1</code>을 반환하면 된다.</li>
</ul>

<h5>정확성 테스트 제한 사항</h5>

<ul>
<li>food_times 의 길이는 <code>1</code> 이상 <code>2,000</code> 이하이다.</li>
<li>food_times 의 원소는 <code>1</code> 이상 <code>1,000</code> 이하의 자연수이다.</li>
<li>k는 <code>1</code> 이상 <code>2,000,000</code> 이하의 자연수이다.</li>
</ul>

<h5>효율성 테스트 제한 사항</h5>

<ul>
<li>food_times 의 길이는 <code>1</code> 이상 <code>200,000</code> 이하이다.</li>
<li>food_times 의 원소는 <code>1</code> 이상 <code>100,000,000</code> 이하의 자연수이다.</li>
<li>k는 <code>1</code> 이상 <code>2 x  10^13</code> 이하의 자연수이다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>food_times</th>
<th>k</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[3, 1, 2]</td>
<td>5</td>
<td>1</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>0~1초 동안에 1번 음식을 섭취한다. 남은 시간은 [2,1,2] 이다.</li>
<li>1~2초 동안 2번 음식을 섭취한다. 남은 시간은 [2,0,2] 이다.</li>
<li>2~3초 동안 3번 음식을 섭취한다. 남은 시간은 [2,0,1] 이다.</li>
<li>3~4초 동안 1번 음식을 섭취한다. 남은 시간은 [1,0,1] 이다.</li>
<li>4~5초 동안 (2번 음식은 다 먹었으므로) 3번 음식을 섭취한다. 남은 시간은 [1,0,0] 이다.</li>
<li>5초에서 네트워크 장애가 발생했다. 1번 음식을 섭취해야 할 때 중단되었으므로, 장애 복구 후에 1번 음식부터 다시 먹기 시작하면 된다.</li>
</ul>

### ❌첫번째 풀이 (정확성❌ 효율성❌)
단순히 문제가 시키는대로 푼 풀이이다.
시간이 지날 때마다 순서대로 남은 음식 시간을 1씩 줄이고, 방송 시간은 1씩 늘렸다.
만약 남은 음식 시간이 0이면 다음 음식으로 넘어가고, 이때는 방송 시간은 그대로이다.
방송시간이 K초가 되면, 반복문을 멈추고 다음 먹어야 하는 음식의 순서를 출력한다.
```python
from collections import deque
def solution(food_times, k):
    answer = -1
    idx = 0
    time = 0

    while time < k:
        if food_times[idx]:
            food_times[idx] -= 1
            time += 1
            # print(food_times, time, idx)
        idx = (idx + 1) % len(food_times)

    for i in range(len(food_times)):
        if food_times[idx]:
            answer = idx + 1
            break
        idx = (idx + 1) % len(food_times)
    return answer
```

위 풀이로 정확성 테스트 20번을 제외한 모든 문제를 통과했다.

### ❌두번째 풀이(정확성✅ 효율성❌)
두번째는 큐를 이용해서 풀이했다.
enumerate() 함수를 이용해서 q에 [순서, 음식 시간]을 넣어줬다.
q에서 하나씩 꺼내서 음식 시간을 1씩 줄어주고 남은 시간이 0보다 크다면 다시 q에 넣어주면서 진행했다.
K번 반복 후, q의 제일 앞에 있는 음식의 순서를 return 해주었다.

이 풀이로 정확성 테스트는 모두 통과했지만, 효율성 테스트를 모두 실패했다....
```python
from collections import deque
def solution(food_times, k):
    answer = -1
    q = deque()
    for i, t in enumerate(food_times):
        q.append([i+1, t])
    
    for _ in range(k):
        if not q:
            return answer
        d = q.popleft()
        if d[1]:
            d[1] -= 1
            if d[1]:
                q.append(d)
    if q:
        d = q.popleft()
        answer = d[0]
    
    return answer   
```

### 맞은 풀이

다른 사람들의 풀이를 보고 공부한 결과 이 문제는 다음과 같은 로직으로 풀이해야한다.
>
1. k 값이 충분하면 즉, 음식을 하나 다 먹을 수 있을 만큼 여러번 회전이 가능하면 그에 드는 시간만큼 k 값을 빼주고 heappop을 통해 음식 하나를 제거해줍니다. + 이 과정이 가능할 때 까지 음식을 제거해줍니다.
>
2. 위 과정을 반복하다보면 음식 하나를 다 먹을 수 없을 만큼 k 값이 작아지고 이때부터 heap을 index 기준으로 정렬하여 남은 k 값을 이용해 네트워크 중단 후 먹어야할 음식을 구해줍니다. => 먹어야할 음식의 index = k % len(heap)
[참고](https://kjhoon0330.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%AC%B4%EC%A7%80%EC%9D%98-%EB%A8%B9%EB%B0%A9-%EB%9D%BC%EC%9D%B4%EB%B8%8C-Python)

```python
from heapq import heappush, heappop

def solution(food_times, k):
    # 방송 중단 전 음식을 다 먹는 경우
    if sum(food_times) <= k:
        return - 1
    
    foodHeap = []
    length = len(food_times)    #남은 음식 개수
    for i in range(length):
        heappush(foodHeap, [food_times[i], i + 1]);
    
    time = 0
    while (foodHeap[0][0] - time) * length < k:
        k -= (foodHeap[0][0] - time) * length
        time += (foodHeap[0][0] - time)
        length -= 1
        heappop(foodHeap)
        
    result = sorted(foodHeap, key = lambda x : x[1])    # index를 기준으로 heap을 다시 정렬
    answer = result[k % length][1]
    return answer
```

> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
