# RGB 거리(2) 
# 기존 RGB 거리에서 아래 조건이 추가됨
    # 기존 조건; i(2 ≤ i ≤ N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다
    # 추가 조건;
        # 1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
        # N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
# 집의 수 N(2 ≤ N ≤ 1,000) => O(n^2) ~ O(N log N) 정도 예상 

# 방법: 
    # 각각 색상에 대해 다음을 반복 (총 3번)
        # 첫번째 집 한 색상으로 고정 => dp를 모두 무한대로 초기화 후, 첫번째 색상만 즉 dp[0][start] = arr[0][start] 만 비용 넣어줌
        # (1, N) 까지 dp로 최소합 구해 두기
        # 마지막 집 만큼 다음을 3번 반복
            # 마지막 색상과 처음 고정한 색상이 다를 경우에만 구해 놓은 dp로 답을 업데이트 함

import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * N
for i in range(N) :
    arr[i] = list(map(int, input().split())) # 비용

answer = float('inf')

for start in range(3) : 
    dp = [[float('inf')] * 3 for _ in range(N)]  
    dp[0][start] = arr[0][start] # 1번째 집 색상을 start로 고정 (나머지는 무한대니까 선택 안하겠지)

    for i in range(1, N) :
        dp[i][0] = arr[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = arr[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = arr[i][2] + min(dp[i-1][0], dp[i-1][1])

    for end in range(3) : # 1번째 집과 N번째 집이 다른 경우에만 값을 업데이트
        if start != end : answer = min(answer, dp[N-1][end])

print(answer)