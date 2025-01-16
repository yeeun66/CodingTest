# RGB 거리(2) => 결국 내 풀이의 반례를 찾지 못함. 일단 정석 방법을 참고해서 새롭게 풀어보자.
# 기존 RGB 거리에서 아래 조건이 추가됨
    # 기존 조건; i(2 ≤ i ≤ N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다
    # 추가 조건;
        # 1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
        # N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
# 집의 수 N(2 ≤ N ≤ 1,000) => O(n^2) ~ O(N log N) 정도 예상 

# 방법: < 아마 O(2n) >
    # 원래 RGB 방법으로 답을 구한다. (이전과 다르게 dp는 새로운 배열에 저장하자)
        # 근데 구하는 과정에서 1번째 집과 N번째 집은 인덱스를 표시해둔다.
    # for문 끝난 후, 구한 2개의 인덱스가 같으면, 각각 자신을 제외한 해당 집의 최소 비용을 구한다.
        # 근데 이거 인덱스 찾기 빡셈.. 그래도 해보자
    # 이 최소 비용 두개 중 더 작은 값을 가진 집의 인덱스 값을 1001로 바꾸고 
    # 다시 for문 진행한다.
    # 위 내용을 while문 안에서 진행한 후, 두 인덱스가 다른 값이면 break 하고 최소 dp[n-1] 출력

import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * N
for i in range(N) :
    arr[i] = list(map(int, input().split()))
dp = [[0, 0, 0] for _ in range(N)]
dp[0][0] = arr[0][0]  # 빨강 고정
dp[0][1] = arr[0][1]  # 초록 고정
dp[0][2] = arr[0][2]  # 파랑 고정

# 이 인덱스도 마지막 집까지 업데이트 해줘야 함
idx1 = [-1, -1, -1] 
idx2 = -1
# print(arr)
while True : 
    for i in range(1, N) :
        if dp[i-1][1] < dp[i-1][2] : # R
            if i == 1 : idx1[0] = 1
            else : idx1[0] = idx1[1]
            dp[i][0] = dp[i-1][1] + arr[i][0]
        else : 
            if i == 1 : idx1[0] = 2
            else : idx1[0] = idx1[2]
            dp[i][0] = dp[i-1][2] + arr[i][0]
        if dp[i-1][0] < dp[i-1][2] : # G
            if i == 1 : idx1[1] = 0
            else : idx1[1] = idx1[0]
            dp[i][1] = dp[i-1][0] + arr[i][1]
        else : 
            if i == 1 : idx1[1] = 2
            else : idx1[1] = idx1[2]
            dp[i][1] = dp[i-1][2] + arr[i][1]
        if dp[i-1][0] < dp[i-1][1] : # B
            if i == 1 : idx1[2] = 0
            else : idx1[2] = idx1[0]
            dp[i][2] = dp[i-1][0] + arr[i][2]
        else : 
            if i == 1 : idx1[2] = 1
            else : idx1[2] = idx1[1]
            dp[i][2] = dp[i-1][1] + arr[i][2]
    # print("ss: ", dp)
    # print("idx: ", idx1)
    tmp_min = 1000 * 1000 + 1
    for i in range(3) : # 최종 결과를 가지는 인덱스 추출
        if tmp_min > dp[N-1][i] :
            tmp_min = dp[N-1][i]
            idx2 = i
    if idx1[idx2] == idx2 : 
        min1 = min(arr[0][(idx2+1) % 3], arr[0][(idx2+2) % 3])
        min2 = min(arr[N-1][(idx2+1) % 3], arr[N-1][(idx2+2) % 3])
        if min1 <= min2 :
            arr[0][idx2] = 1000 * 1000 + 1
            dp[0][0] = arr[0][0]  # 빨강 고정
            dp[0][1] = arr[0][1]  # 초록 고정
            dp[0][2] = arr[0][2]  # 파랑 고정

        else : arr[N-1][idx2] = 1000 * 1000 + 1
    else :
        print(tmp_min)
        break