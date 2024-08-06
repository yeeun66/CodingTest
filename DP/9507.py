# 좀더 복잡한 피보나치를 만들어보고자 한다.
# n < 2 :                         1
# n = 2 :                         2
# n = 3 :                         4
# n > 3 : koong(n − 1) + koong(n − 2) + koong(n − 3) + koong(n − 4)

# 첫번째 줄: TC 갯수, 다음 줄: 구해야 하는 피보나치 수 번호 n

import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n) :
    a = int(input())
    if a == 0 or a == 1: 
        print(1)
        continue
    if a == 2: 
        print(2)
        continue
    if a == 3: 
        print(4)
        continue

    dp = [0] * (a+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, a+1) :
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]
    print(dp[a])