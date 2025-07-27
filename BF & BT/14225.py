# 부분수열의 합
# 수열 S의 부분 수열의 합으로 나올 수 없는 가장 작은 자연수 구하기
'''
로직
1. 수열 오름차순 정렬 
2. 백트래킹 탐색
    - 중복 없이 모든 경우 탐색 (리스트에 넣지말고 그냥 sum으로 하면 됨)
    - 모든 현재 sums 값을 set에 모두 저장해둠
3. 백트래킹 이후 1부터 탐색하며 set에 없으면 출력후 종료

'''

import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))
# check = [0] * 100001  # sums는 10만 이상일수도 있음.. 
check = set() # set 에 모든 sum 다 넣어놓고, 나중에 없는 것 중 최소 뽑기
S.sort()

def backtrack(sums, idx, depth) : # 현재 부분 수열의 합한 값, 마지막 인덱스 
    if depth == N : 
        return
    
    for i in range(N) :
        if i <= idx : continue
        sums += S[i]
        check.add(sums)
        backtrack(sums, i, depth+1)
        sums -= S[i]
    
arr = []
backtrack(0, -1, 0)

i = 0
while True : 
    i += 1
    if i not in check : 
        print(i)
        exit()