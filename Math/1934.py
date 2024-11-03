# 최소 공배수
# 공통 배수 중 가장 작은 배수

# 로직: 둘 중 큰 걸 골라서 그 수 부터 a*b 까지
# 1씩 증가 시키면서 2개 모두 나누어 떨어지면 그 때 i가 최소 공배수
# => 이거 시간 초과 떠서 유클리드 호제법 써야할듯

# 그냥 math 함수가 가장 빠르다!

import sys
import math
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    print(math.lcm(a, b))
    # for i in range(max(a, b), (a*b)+1) :
    #     if i % a == 0 and i % b == 0 :
    #         print(i)
    #         break