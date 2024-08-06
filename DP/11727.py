# 2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성
# 첫째 줄에 입력 n
# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력

# 하나씩 해보면 점화식이 나올지도 
# n = 1 : 1
# n = 2 : 3
# n = 3 : 5
# n = 4 : 11
# n = 5 : 21
# n = 6 : 37 뭐냐 이게 
# --> Fn = 2(n-2) + (n-1) 이걸 생각할 수 있도록 하쟈...

import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

if(n == 1) : 
    print(1)
elif(n == 2) : 
    print(3)
else:
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n+1) :
        dp[i] = (dp[i-1] + 2 * dp[i-2]) % 10007 # 여기에 마드해!!!

    print(dp[n], end=' ')