# N!을 출력하는 프로그램

import sys
input = sys.stdin.readline

N = int(input())

result = 1
for i in range(2, N+1) :
    if N == 0 or N ==1: 
        print(1)
        break
    result *= i
print(result)