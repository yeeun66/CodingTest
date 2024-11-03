# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# 최대 공약수: 공통 약수들 중 가장 큰 것
# 최소 공배수: 공통 배수들 중 가장 작은 것

# 1. math 함수 사용
# 2. 그냥 일반적인 로직
# 3. 유클리드 호제법
    # https://codingpractices.tistory.com/entry/Python-최소공배수-최대공약수란-알고리즘-쉽게-이해하기

# 입력
# 24 18
# 출력
# 6
# 72

import sys
import math
input = sys.stdin.readline

a, b = map(int, input().split())
print(math.gcd(a, b))
print(math.lcm(a, b))