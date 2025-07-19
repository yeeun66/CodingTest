# N과 M (8) - 백트래킹 연습
# M개 고르기. 중복 가능 
# 비내림차순이어야 함. 즉 오른쪽이 왼쪽보다 커서는 안됨

N, M = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()

def backtrack() :
    if len(arr) == M : 
        print(*arr)
        return
    
    for i in range(0, N) :
        if not arr :
            arr.append(n_list[i])
            backtrack()
            arr.pop()

        elif n_list[i] >= arr[-1] : 
            arr.append(n_list[i])
            backtrack()
            arr.pop()

arr = []
backtrack()