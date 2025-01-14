# 골드바흐 파티션 (골드바흐 추측과 유사)

# 8 = 3 + 5, 8 = 5 + 3 처럼 소수를 통해 표현 가능한 8은 2가지로 가능하다. 따라서 골드 바흐의 파티션은 6이다
# 마찬가지로 6 = 3 + 3 은 1가지 이다. 이러한 가지수를 출력한다. (이때, 순서가 다른 것은 같은 파티션으로 침)
    # => 카운트 제대로 하려면 카운트 전에 새로운 배열에 저장되어 있던 소수이면 카운트하지 않음 조건 추가
# 이전 코드에서 출력 대신 가능한 가지수에 count를 한 것을 출력하면 됨

import sys
input = sys.stdin.readline
T = int(input())

# 소수 부터 먼저 만들어 놓기
pri = [1] * 1000001
pri[1] = 0
primes = []
for i in range(2, 1000001) :
    if pri[i] == 0 : continue
    for j in range(i*i, 1000001, i)  :
        pri[j] = 0
    primes.append(i)

# 파티션 찾기
for _ in range(T) :
    n = int(input())
    count = 0
    for i in primes :
        if i > (n/2) : break
        diff = n - i
        if pri[diff]: 
            count += 1
    
    print(count)