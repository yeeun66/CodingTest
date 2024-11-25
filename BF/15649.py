# N과 M (1)
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# >> 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

# 로직: DFS는 전부 탐색.
# 백트래킹은 DFS 활용) 이미 방문한 경우 제외. continue <-- 가지치기

# backtracking 함수 - 재귀
    # array 길이 == m : 결과 출력 후 리턴
    # 1부터 N까지 반복 <- 자식 노드에 대해
        # 이 수가 array에 없다면: <- 정답에 유망
            # array에 해당 숫자 추가
            # backtracking() <-- 재귀 호출
            # array에 끝원소 pop <-- 부모로 이동

import sys
input = sys.stdin.readline

def backtracking() :
    if len(array) == M : 
        print(" ".join(map(str, array))) # M개 채워지면 결과 출력
        return

    for i in range(1, N+1) : 
        if i not in array :
            array.append(i)
            backtracking() # 재귀
            array.pop()

N, M = map(int, input().split())
array = [] # 빈 array 생성

backtracking()