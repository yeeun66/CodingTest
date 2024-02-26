# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램
# 
# 와 이게 시간초과라고? -> 누적합 알고리즘 써야 함

# - 누적합 알고리즘
#     1. 먼저 처음에서부터 누적된 합을 구해놓는다
#     2. 필요한 구간의 마지막 지점 누적합에서 시작 지점의  앞 구간 누적합을 빼면 됨!
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
list = list(map(int, input().split()))

total = 0
sum_list = [] # 누적합 리스트 
for a in list :     
    total += a
    sum_list.append(total)

for _ in range(M) : # M: test case 갯수
    i, j = map(int, input().split())
    if i == 1 : result = sum_list[j-1]
    else : result = sum_list[j-1] - sum_list[i-2]
    print(result)