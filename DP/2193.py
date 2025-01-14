# 이친수 (pinary number)
# 이친수는 다음의 성질을 만족한다.
    # 이친수는 0으로 시작하지 않는다.
    # 이친수에서는 1이 두 번 연속으로 나타나지 않는다. 즉, 11을 부분 문자열로 갖지 않는다.
# N(1 ≤ N ≤ 90)이 주어졌을 때, N자리 이친수의 개수를 구하는 프로그램을 작성

# 일단 N = 6까지 했을 때 발견한 규칙 
# d[i][1] = d[i][0] - d[i-1][1] # 이 때 i는 자릿수(N), j는 끝자리(0또는1)
# d[i][0] = d[i-1][0] + d[i-1][1]

import sys
input = sys.stdin.readline
N = int(input())
dp = [[0 for _ in range(2)] for _ in range(N+1)]

if N == 1 : 
    print(1)
    exit()

dp[1][1], dp[2][0] = 1, 1

for i in range(2, N+1) :
    for j in range(2) :
        if j == 1: dp[i][1] = dp[i][0] - dp[i-1][1]
        elif j == 0: dp[i][0] = dp[i-1][0] + dp[i-1][1]

print(sum(dp[N]))