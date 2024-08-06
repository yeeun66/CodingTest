# 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
# 1부터 n까지의 번호가 붙어 있는 n개의 포도주 잔이 있을 때,
# 가장 많은 양의 포도주를 마실 수 있도록 하는 프로그램을 작성

import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * n
amount = []
for _ in range(n) :
    x = int(input())
    amount.append(x)

dp[0] = amount[0]
if n > 1 : dp[1] = max(amount[0] + amount[1], amount[1]) 
if n > 2 : dp[2] = max(amount[1] + amount[2], amount[0] + amount[2], dp[1]) # 자신을 선택하지 않는 것도 좋은 방법이 될 수 있다

for i in range (3, n) :
        dp[i] = max(amount[i] + amount[i-1] + dp[i-3], amount[i] + dp[i-2], dp[i-1])

print(max(dp))