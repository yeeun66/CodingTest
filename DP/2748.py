# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성
# Fn = Fn-1 + Fn-2 (n ≥ 2)

import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1)
dp[0] = 0 
dp[1] = 1

for i in range(2, n+1) :
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])