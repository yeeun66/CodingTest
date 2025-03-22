# N과 M (4) - 백트래킹 연습
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성
    # 1부터 N까지 자연수 중에서 M개를 고른 수열
    # 같은 수를 여러 번 골라도 된다.
    # 고른 수열은 비내림차순이어야 한다

# 1. 백트래킹 함수 구현
    # 1-1. 현재 배열에 M개가 들어있으면 배열 출력 후 함수 리턴
    # 1-2. 반복문 (1부터 N+1)까지 반복하며 백트래킹 수행
        # 현재 배열의 값이 없거나, 비내림 차순 만족하면, 배열에 추가
        # 재귀 호출
        # 배열에서 pop
        
N, M = map(int, input().split())

def backtracking() : 
    if len(arr) == M :
        print(" ".join(map(str, arr)))
        return
    
    for i in range(1, N+1) :
        if not arr or arr[-1] <= i : 
            arr.append(i)
            backtracking()
            arr.pop()
    
arr = []   
backtracking()