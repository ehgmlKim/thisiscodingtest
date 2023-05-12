def solution(s):
    answer = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s)//2+1):
        result = ''
        temp = s[:i]
        count = 1
        for j in range(i, len(s), i):
            if temp == s[j:i+j]:
                count += 1
            else:
                if count == 1:
                    result += temp
                else:
                    result += str(count) + temp
                count = 1
                temp = s[j:i+j]
        if count == 1:
            result += temp
        else:
            result += str(count) + temp
        answer.append(len(result))
    return min(answer)