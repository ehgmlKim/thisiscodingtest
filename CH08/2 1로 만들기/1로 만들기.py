import sys
input = sys.stdin.readline

x = int(input())
dp = [0 for i in range(x+1)]
#최소 연산 횟수를 찾는 것이므로
#각 배열의 인덱스를 x의 값의 변호로 보고
#해당 값으로 만들기까지의 연산 횟수를 해당 인덱스의 값으로 한다.

for i in range(2, x+1): #x가 1일 때는 생각해줄 필요 없음
    dp[i] = dp[i-1] + 1
    if i%5==0:
        dp[i] = min(dp[i], dp[i//5]+1)
    if i%3==0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i%2==0:
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[x])