# 45656이란 수를 보자.
# 이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.
# N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0으로 시작하는 수는 계단수가 아니다.
# 첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.

# 아니 이거
# d[i][j]를 i자리 수 중에 j로 끝나는 수의 갯수라 두고
# 액셀에 갯수를 세보면 d[i][j] = d[i-1][j-1] + d[i-1][j+1] 임을 알 수 있음 (규칙성)
    # 물론 j = 0, 9 일 때 제외

import sys
input = sys.stdin.readline

N = int(input())
dp = [[0 for _ in range(10)] for _ in range(N+1)] # i = N+1, j = 10 크기의 2차원 d[i][j]

for j in range(1, 10) : dp[1][j] = 1 # 한자리수 일 땐 1로 초기화
for i in range(2, N+1) :
    for j in range(10) :
        if j == 0 : dp[i][j] = dp[i-1][j+1]
        elif j == 9 : dp[i][j] = dp[i-1][j-1]
        else : dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N])%1000000000)