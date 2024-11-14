# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램

import sys
input = sys.stdin.readline

N = int(input())

result = 1
for i in range(2, N+1) :
    if N == 0 or N ==1: 
        print(1)
        break
    result *= i

result = list(str(result))
result = result[::-1]

count = 0
for i in result :
    if i == '0' : count += 1
    else : break
print(count)