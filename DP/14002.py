# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 
# 가장 긴 증가하는 부분 수열은 A = {10, 20, 30, 50} 이고, 길이는 4이다.

# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
# 둘째 줄에는 가장 긴 증가하는 부분 수열을 출력한다. 
# 그러한 수열이 여러가지인 경우 아무거나 출력한다.
# 수열 튜플로 업데이트 하지 말고 그냥 리스트로 하기 > 출력하기 너무 힘듦

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

output = []
[output.append([]) for _ in range(N)]
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i) :
        if A[i] > A[j] : 
            if dp[j] + 1 > dp[i] : 
                dp[i] = dp[j] + 1
                output[i].clear()
                for a in output[j] :
                    output[i].append(a)
    output[i].append(A[i])

maxx = max(dp)
idx = dp.index(maxx)

print(maxx)
print(*output[idx])