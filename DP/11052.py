# 카드 팩의 가격이 주어졌을 때, N개의 카드를 구매하기 위해 민규가 지불해야 하는 금액의 최댓값을 구하는 프로그램을 작성하시오

# 카드의 개수가 적은 팩이더라도 가격이 비싸면 높은 등급의 카드가 많이 들어있을 것이라는 미신을 믿고 있다. 
# 따라서, 민규는 돈을 최대한 많이 지불해서 카드 N개 구매하려고 한다. 카드가 i개 포함된 카드팩의 가격은 Pi원이다.

# 4
# 1 5 6 7
# --> 10

# dp[1] = 1
# dp[2] = max(dp[2], dp[1] + P[1]) # 본인 넣기 vs 본인 빼고 이전 dp + 이전 p
# dp[3] = max(dp[3], dp[1] + P[3-1]) # 1개 + 2개
# dp[3] = max(dp[3], dp[2] + P[3-2]) # 2개 + 1개

# dp[4] = max(dp[4], dp[1] + P[4-1]) # 1개 + 3개
# dp[4] = max(dp[4], dp[2] + P[4-2]) # 2개 + 2개
# dp[4] = max(dp[4], dp[3] + P[4-3]) # 3개 + 1개

import sys
input = sys.stdin.readline

N = int(input())
# dp랑 원래 값 저장할 배열을 분리
dp = [0 for _ in range(N+1)] # 최대값을 저장 & 업데이트 해줄 dp 배열
P = list(map(int, input().split())) # 원래 값 넣을 배열
P.insert(0,0) # 0번째 안쓸거니까

dp[1] = P[1]

for i in range(2, N+1) : # 2, 3, 4
    dp[i] = P[i] # 일단 i개 산다고 할 때, i개 다 사는 경우의 값을 dp에 저장
    for j in range(1, i) : # j는 1부터 본인 전까지
        dp[i] = max(dp[i], dp[j]+P[i-j]) # dp 값 계속 최대로 수정

print(dp[N])