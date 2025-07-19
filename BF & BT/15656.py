# N과 M (7) - 백트래킹 연습
# M개 고르기. 중복 가능 
# 오름차순 정렬

N, M = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()

def backtrack() :
    if len(arr) == M : 
        print(*arr)
        return
    
    for i in range(0, N) :
        arr.append(n_list[i])
        backtrack()
        arr.pop()

arr = []
backtrack()