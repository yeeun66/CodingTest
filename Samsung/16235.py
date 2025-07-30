# 나무 재테크
'''
로직 - 시간초과
상태 관리
- N*N 보드: 양분 관리 (초기 양분은 모두 5)
- live_tree: 살아있는 나무 관리 (좌표, 나이)
- dead_tree: 봄에 죽은 나무 관리
아래를 k번 반복
1. 봄) 각 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가함
    - 하나의 칸에 여러개의 나무가 있으면 어린 나무부터 양분 먹음
        - live_tree 정렬 후 수행
    - 현재 땅의 양분이 나무의 나이보다 작아서 먹지 못하면 그 나무는 죽음
        - live_tree에서 제거 후, dead_tree에 추가
2. 여름) dead_tree가 양분으로 변함
    - 해당 칸에 죽은 나무의 나이를 2로 나눈 몫을 양분으로 추가
3. 가을) 나무 번식
    - 나이가 5배수인 나무에 대해 번식
    - 인접 8칸에 나이가 1인 나무가 생김 -> live_tree에 업데이트
4. 겨울) 땅에 양분 추가
    - 각 칸에 A[r][c]만큼의 양분이 추가됨 (입력으로 줌)

반복 종료후 live_tree의 개수 출력
'''

'''
(시간초과 해결 로직) - 이거 시간제한 비정상적으로 너무 빡셈.. 
봄 - 여름을 한번에 수행 
가을 - 겨울도 한번에 수행 
원래 매 봄마다 sort()로 정렬 해줬는데 - 이게 시간 많이 잡아먹었던 듯
    -> 처음 한번만 솔팅하고 나머지는 큐로 관리하면 자연스럽게 가장 어린게 앞에 오게 됨
'''

from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = []
for _ in range(N) : A.append(list(map(int, input().split())))
live_tree = []
for _ in range(M) : 
    x, y, z = map(int, input().split())
    live_tree.append((z, x-1, y-1))
board = [[5 for _ in range(N)] for _ in range(N)]

live_tree.sort() # 처음에만 솔팅 - 다음부터는 큐로 관리
live_tree = deque(live_tree)

def is_inrange(x, y) : 
    return 0<=x<N and 0<=y<N

def spring_summer() : 
    new_live_tree = deque()
    new_board = [b[:] for b in board]
    # live_tree.sort() # 이거 매번 솔팅해서 그런가..? 
    
    while live_tree : 
        z, x, y = live_tree.popleft()
        if board[x][y] >= z : 
            board[x][y] -= z
            new_board[x][y] -= z # 봄
            new_live_tree.append((z+1, x, y))
        else : 
            new_board[x][y] += (z // 2) # 여름 
    
    return new_live_tree, new_board

def fall_winter() : 
    new_live_tree = deque()
    for z, x, y in live_tree : 
        if z % 5 != 0 : continue
        for nx, ny in (x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1):
            if not is_inrange(nx, ny) : continue
            new_live_tree.append((1, nx, ny))
    
    new_live_tree.extend(live_tree) # 새로운거에 예전꺼 붙여주기 
    
    for i in range(N) : 
        for j in range(N) : 
            board[i][j] += A[i][j]
    
    return new_live_tree
    
for _ in range(K) : 
    live_tree, board = spring_summer() # 봄, 여름 
    if not live_tree : # 나무 없으면 그냥 종료
        print(0)
        exit()
    
    live_tree = fall_winter() #가을, 겨울 

print(len(live_tree))