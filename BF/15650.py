# N과 M (2)
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
    # >> 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
    # >> 고른 수열은 오름차순이어야 한다.
# 이전 문제 N과 M (1) 에서 백트래킹 조건 하나만 추가
# 조건: 오름차순으로만 추가. 즉 이전 값보다 커야 array에 추가 가능

import sys
input = sys.stdin.readline

def backtracking():
    if len(array) == M :
        print(" ".join(map(str, array)))
        return

    for i in range(1, N+1) :
        if i not in array :
            if not array or array[-1] < i :
                array.append(i)
                backtracking()
                array.pop()

N, M = map(int, input().split())
array = []
backtracking()