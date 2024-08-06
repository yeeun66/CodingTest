# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우
# 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4
# 완성 dp = [1, 2, 1, 3, 2, 4]

N = int(input()) # 수열의 크기

a = list(map(int, input().split())) # 각 수열에 해당하는 숫자

dp = [1] * N # A[i]를 마지막 값으로 가지는 가장 긴 증가 부분 수열의 길이 (전체가 되면 부분도 되어야 한다)

for i in range(1, N) :
    for j in range(i) :
        if a[i] > a[j] :
            dp[i] = max(dp[i], dp[j] + 1)
# print(dp)
print(max(dp), end=' ')