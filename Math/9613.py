# 양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램
# GCD의: 최대 공약수 
# 입력: 
# 3
# 4 10 20 30 40
# 3 7 5 12
# 3 125 15 25
# 출력: 
# 70
# 3
# 35

import sys
import math
input = sys.stdin.readline

t = int(input())
for _ in range(t) :
    sum = 0
    arr = list(map(int, input().split()))
    l = len(arr)
    for i in range(1, l) :
        for j in range(i+1, l) :
            if i == j : continue
            else : sum += math.gcd(arr[i], arr[j])
    print(sum)