# N과 M (6) - 백트래킹 연습

# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.
    # N개의 자연수 중에서 M개를 고른 수열
    # 고른 수열은 오름차순이어야 한다. 

# 로직
# 일단 사전순으로 정렬 
# arr에 추가하는 조건에서, 현재 끝 원소가 자신보다 작을때만 추가

N, M = map(int, input().split())
n_list = list(map(int, input().split()))
n_list = sorted(n_list)

def backtrack() :

    if len(arr) == M :
        print(' '.join(map(str, arr)))
        return
    
    for n in n_list : 
        if n not in arr:
            if arr and arr[-1] > n : continue
            arr.append(n)
            backtrack()
            arr.pop()
    
arr = []
backtrack()