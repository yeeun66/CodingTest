# N과 M (5) - 백트래킹 연습
# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.
# N개의 자연수 중에서 M개를 고른 수열

#  중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

# 로직
# n_list에 N개의 자연수를 저장해둔다 - 아 이걸 바로 솔팅을 하면 원래 처럼 바로 출력해도 될지도
# 백트래킹 - 

N, M = map(int, input().split())
n_list = list(map(int, input().split()))

n_list = sorted(n_list) # 첫 배열을 그냥 솔팅하면 사전순으로 증가함

def backtrack() :
    if len(arr) == M : 
        print(' '.join(map(str, arr)))
        return
    
    for n in n_list :
        if n not in arr : 
            arr.append(n)
            backtrack()
            arr.pop()

arr = [] # 백트래킹에서 사용
backtrack()