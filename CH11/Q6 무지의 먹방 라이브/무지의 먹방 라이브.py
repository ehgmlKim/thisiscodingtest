from collections import deque


def solution(food_times, k):
    answer = -1
    idx = 0
    time = 0
    q = deque()
    for i, t in enumerate(food_times):
        q.append([i + 1, t])

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
