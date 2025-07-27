# 링크와 스타트
# 스타트 팀의 능력치와 링크 팀의 능력치의 차이의 최솟값 출력 
'''
로직
1. 백트래킹으로 모든 나누는 경우의 수 탐색 - backtrack(arr, depth)
    - 4명이라면,
        - 1 / 2, 3, 4
        - 1, 2 / 3, 4
        - 1, 3 / 2, 4
        - 1, 4 / 2, 3
        - 1, 2, 3 / 4
        - 1, 2, 4 / 3
        - 1, 3, 4 / 2
    - 위 예시와 같이 1번 선수는 무조건 스타트팀
    
    - 1 < l < N : power_sum(arr) 수행
    - Base case : depth == N -> 그냥 리턴

2. 각 경우의 수 마다 각 팀의 능력치 합의 차이 구해서 최솟값 업데이트 - power_sum
    - 백트래킹에서 가져온 lst는 스타트 팀 / 포함 안된 나머지는 링크 팀
    - 각 능력치 합 구한후 차이 구하고 현재 최솟값과 비교후 업데이트 
3. 최종 최솟값 출력
'''
import sys
input = sys.stdin.readline
N = int(input())
S = []
visit = set()
for _ in range(N) : S.append(list(map(int, input().split())))

min_diff = int(1e9)
def power_sum(start) : 
    global min_diff

    num = len(start) # 스타트 팀 인원
    link = []
    for i in range(1, N+1) : 
        if i not in start : 
            link.append(i)
    
    start_sum, link_sum = 0, 0
    for i in range(num) : 
        for j in range(i+1, num) : 
            x, y = start[i]-1, start[j]-1
            start_sum += S[x][y]
            start_sum += S[y][x]
    
    for i in range(N-num) : 
        for j in range(i+1, N-num) : 
            x, y = link[i]-1, link[j]-1
            link_sum += S[x][y]
            link_sum += S[y][x]
    
    min_diff = min(min_diff, abs(start_sum-link_sum))
    

def backtrack(arr, idx, depth) : 
    if depth == N : return
    
    if depth > 0 and tuple(arr) not in visit : 
        power_sum(arr)
        # print(arr)
        visit.add(tuple(arr))

    for i in range(1, N+1) : 
        if i > idx : 
            arr.append(i)
            backtrack(arr, i, depth+1)
            tmp = arr.pop()
            if tmp == 1 : break
        

backtrack([], -1, 0)
print(min_diff)
