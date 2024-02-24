# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램
# 
# 와 이게 시간초과라고? -> 누적합 알고리즘 써야 함
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
list = list(map(int, input().split()))

for _ in range(M) :
    i, j = map(int, input().split())
    sum = 0
    for a in range(i-1, j) :
        sum += list[a]
    print(sum)