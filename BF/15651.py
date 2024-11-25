# N과 M (3)
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
    # 1부터 N까지 자연수 중에서 M개를 고른 수열
    # 같은 수를 여러 번 골라도 된다.

# N과 M (1) 에서 백트래킹 조건 변경
# i가 array에 없으면 <- 이 조건을 지우면 됨

import sys
input = sys.stdin.readline

def backtracking():
    if len(array) == M :
        print(" ".join(map(str, array)))
        return

    for i in range(1, N+1) :
        array.append(i)
        backtracking()
        array.pop()

N, M = map(int, input().split())
array = []
backtracking()