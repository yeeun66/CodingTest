# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N = int(input())
count = 0
arr = []
arr = list(map(int, input().split()))

for x in arr :
    flag = 0
    if x == 1: continue
    elif x == 2 : 
        count += 1
        continue

    for i in range(2, x) : 
        if x % i == 0 : 
            flag =1
            break

    if flag == 0 : count += 1 # 약수가 자기 밖에 없는 것을 카운트
print(count)
