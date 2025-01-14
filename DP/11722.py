# 가장 긴 감소하는 부분 수열

# 수열 A = {10, 30, 10, 20, 20, 10} 인 경우에 
# 가장 긴 감소하는 부분 수열은 A = {10, '30', 10, '20', 20, '10'}  이고, 
# 길이는 3이다. => 길이 출력
# 이때 결과 dp 배열은 [1, 1, 2, 2, 2, 3] 으로 완성됨. 따라서 max값 3 출력
# 각 해당 수열에 대해 이전 수열 모두 탐색하며
    # 본인 보다 큰 것이 있으면,
    # 본인 dp = max(그 큰것의 dp + 1, 본인 dp)

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * (n)

for i in range(n) :
    for j in range(i) :
        if arr[j] > arr[i] : dp[i] = max(dp[j]+ 1, dp[i])
print(max(dp))