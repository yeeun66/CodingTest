# 0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하는 프로그램을 작성
# N / k 2차원 배열로 표 그려보면 dp[i][j] = dp[i-1][j] + dp[i][j-1] 이라는 거 눈으로 확인 가능

# 중복 조합으로 푸는 방식도 있다고 함.. 나는 이거 몰라

import sys
input =  sys.stdin.readline

N, K = map(int, input().split())

dp = [[ (i + 1) for i in range(K)] for _ in range(N)]

for i in range(1, N) :
    for j in range(1, K) :
        dp[i][j] = dp[i-1][j] + dp[i][j-1] 

print(dp[N-1][K-1] % (1000000000), end=' ')
# print(dp)