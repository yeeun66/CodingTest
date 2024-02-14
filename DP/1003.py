# 피보나치 함수

# N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성
# 문제에서 C++ code 제공

T = int(input())

dp_zero = [0] * 41
dp_one = [0] * 41

dp_zero[0] = 1
dp_one[1] = 1
for _ in range(T) :
    n = int(input())
    for i in range(2, n+1) :
        dp_zero[i] = dp_zero[i-1] + dp_zero[i-2]
        dp_one[i] = dp_one[i-1] + dp_one[i-2]
    print(dp_zero[n], end=' ')
    print(dp_one[n])