# 골드바흐의 추측

# 1. 입력 받은 n 보다 작은 소수 구하기 
    # -> 에라토스테네스의 체 알고리즘(2를 제외한)
# 2. 이 소수들로 n 만들기 
    # 가능 하다면, n = a + b 이런식으로 출력하고 break
    # 반복 다 했는데 불가능 하면, "Goldbach's conjecture is wrong." 출력

    # 가능 한지 판별하는 법
        # 예를 들어, 8 미만의 소수는 3,5,7이다 (2 제외)
        # for문 한번 돌면서 n - primes[i] 를 한다
            # 방금 한게 primes 내부에 있으면 True
            # 없으면 False
        # 최종적으로 False 이면 없는겨

# 시간 초과..
# Sol1)
    # 8이하의 소수 3개를 구했는데
    # 20이하의 소수 구할 때 이걸 또 계산할 필요는 없다고 생각됨
        # 1. 소수 구하기)) 입력을 그냥 한번에 다 받고 거기서 최대 값에 해당하는 짝수 미만의 소수를 미리 다 찾는다
        # 2. 소수로 n 만들기)) 원래 방식으로 n 만들기 하되, i번째가 소수가 n보다 큰 경우에도 반복 중단

# Sol2)
    # 입력 받은 숫자 중 max 구하지 말고 그냥 1000001 까지의 소수 구해놓기
        # 이때 소수인지(1), 소수가 아닌지(0) 판별하는 배열 선언 하고 1로 초기화 후, 
        # 소수가 아니면 0으로 만들기

# ------- solution 2 ------ (성공!!)
import sys
input = sys.stdin.readline

## 소수 구하기 시작 ## <- 1000001 까지
pri = [1 for i in range(1000001)] # 소수 판별 위한 배열 / 소수면(1) 아니면(0)
primes = [] # 소수 넣는 곳
for i in range(2, 1000001) : 
    if pri[i] == 0: continue # 소수가 아니면 통과
    for j in range(i*i, 1000001, i) : # 해당 소수의 배수부터는
        pri[j] = 0 # 모조리 소수가 아닌 것으로 판단

    primes.append(i) # 소수를 오름차순으로 저장

while True:
    # 소수로 n 만들기 시작 ##
    n = int(input())
    if n == 0: break
    flag = 0
    for i in primes :
        if i > n : break
        diff = n - i
        if pri[diff] : # 소수이면
            print(n, "=", i, "+", diff)
            flag = 1
            break
        
    if not flag : print("Goldbach's conjecture is wrong.")

# ------- solution 1 ------ (시간 초과)

# import sys
# input = sys.stdin.readline

# num = []
# while True : # 일단 입력만 받기
#     n = int(input())
#     if n == 0 : break
#     num.append(n)

# ## 소수 구하기 시작 ## <- 최대값 까지
# max_num = max(num)
# primes = [3] # 소수들 저장할 곳
# maxxx = int(max_num**(1/2))
# for i in range(5, max_num, 2) : # 3부터 max_num미만 사이의 소수를 찾을 거임
#     pr = 0
#     for j in range(3, maxxx+1) :
#         if i == j : continue
#         if i % j == 0 : # i는 소수가 아닌 것
#             pr  = 1
#             break
#     if not pr : primes.append(i)

# for n in num :
#     # 소수로 n 만들기 시작 ##
#     l = len(primes)
#     flag = 0
#     l = int(l/2)
#     for i in range(l+1) :
#         if i > n : break
#         diff = n - primes[i]
#         if diff in primes :
#             print(n, "=", primes[i], "+", diff)
#             flag = 1
#             break
        
#     if not flag : print("Goldbach's conjecture is wrong.")

# ------- original solution ------ (시간 초과)

# import sys
# input = sys.stdin.readline

# while True :
#     n = int(input())
#     if n == 0 : break

#     ## 소수 구하기 시작 ##
#     primes = [3] # 소수들 저장할 곳
#     maxxx = int(n**(1/2))
#     for i in range(5, n, 2) : # 3부터 n미만 사이의 소수를 찾을 거임
#         pr = 0
#         for j in range(3, maxxx+1) :
#             if i == j : continue
#             if i % j == 0 : # i는 소수가 아닌 것
#                 pr  = 1
#                 break
#         if not pr : primes.append(i)

#     # print("primes: ",  primes)
#     ## 소수로 n 만들기 시작 ##
#     l = len(primes)
#     flag = 0
#     l = int(l/2)
#     for i in range(l+1) :
#         diff = n - primes[i]
#         if diff in primes :
#             print(n, "=", primes[i], "+", diff)
#             flag = 1
#             break
        
#     if not flag : print("Goldbach's conjecture is wrong.")