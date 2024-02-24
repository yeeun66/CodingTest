# 계단 오르기
# 1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다.
# 2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 3. 마지막 도착 계단은 반드시 밟아야 한다.

# 각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램

# - 마지막 계단 무조건 밟아야 하니까 두 가지로 분류 가능
#     1. 전 칸을 밟고 마지막 칸 밟는 경우
#         1. 이 때, 연속 세 칸은 불가능 하므로  마지막 칸이 n칸일 때, n-2번째 칸을 밟을 수 없음
#     2. 전전칸 밟고 마지막 칸 밟는 경우 
# - DP 배열 생성 후 , 거기에 n칸까지의 최대값을 저장. 즉, 조건 두 개중 최대값을 저장

# 인덱스 에러 났던 이유: 계단 1개만 있을 때도 dp[1], dp[2] 초기화 했어서 조건 붙여서 해결

import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N)
score = []
for _ in range(N) :
    x = int(input())
    score.append(x)

dp[0] = score[0]
if (N > 1) : dp[1] = max(score[1] + score[0], score[1])
if (N > 2) : dp[2] = max(score[2] + score[1], score[2] + score[0])

for i in range(3, N) :
    dp[i] = max(score[i] + score[i-1] + dp[i-3], score[i] + dp[i-2])

print(dp[N-1])