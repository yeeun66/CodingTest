# 두 자연수 A와 B가 있을 때, A = BC 를 만족하는 자연수 C를 A의 약수라고 한다. 
# 예를 들어, 2의 약수는 1, 2가 있고, 24의 약수는 1, 2, 3, 4, 6, 8, 12, 24가 있다. 
# 자연수 A의 약수의 합은 A의 모든 약수를 더한 값이고, f(A)로 표현한다. 
# x보다 작거나 같은 모든 자연수 y의 f(y)값을 더한 값은 g(x)로 표현한다.

# 자연수 N이 주어졌을 때, g(N)을 구해보자.

# 시간초과 해결법 - 하나 하나 구하는게 아니고 머리를 쓰자!
# N = 4 일 때
# f(1) = 1
# f(2) = 1 + 2
# f(3) = 1 + 3
# f(4) = 1 + 2 + 4

# g(4) = 1*4 + 2*2 + 3*1 + 4*1
# = k*(n//k)

import sys
input = sys.stdin.readline

n = int(input())
print(sum(k*(n//k) for k in range(1, n+1)))