# 소인수분해

# 1. N 이하의 소수 생성 (에라토스테네스의 체)
# 2. N이 1이 될 때 까지 나눠줌
    # 소수 저장한 배열 오름차순으로 시작해서
    # 해당 소수로 %한 결과가 0이면 해당 소수 출력 후 N // 해당  소수 진행

import sys
input = sys.stdin.readline

N = int(input())
if N == 1 : exit()

pri = [1] * (N+1)
primes = []
for i in range(2, N+1) :
    if pri[i] == 0 : continue
    for j in  range(i*i, N+1, i) :
        pri[j] = 0
    primes.append(i)

for i in primes :
    if N == 1 : break
    while N % i == 0 :
        print(i)
        N /= i