# 토마토2 (토마토 업그레이드 문제) -- 2차원을 3차원으로 바꿔서 풀기

# graph[H][N][M]
# 접근 가능: 
# 1. 같은 graph[H] 에서의 상하좌우 탐색
# 2. graph[H]는 다르지만 (H-1, H+1) 나머지 좌표가 일치하는 경우

import sys
from collections import deque

input = sys.stdin.readline

def bfs(onee, one_poss):
    day = -1
    queue = deque()
    for i in range(onee) :
        x, y, z = one_poss[i]
        queue.append((x, y, z))

    while queue : 
        x, y, z = queue.popleft()
       
        for i in range(6) :
            
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and graph[nx][ny][nz] == 0 :
                graph[nx][ny][nz] = 1
                queue.append((nx, ny, nz))

        onee -= 1
        if onee == 0 :
            day += 1
            onee = len(queue)
    
    for i in range(H): # 모든 작업을 했는데도 0이 남아있는 경우 익을 수 없는 토마토
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 0 :
                    print("-1")
                    return
    print(day)
            
            
M, N, H = map(int, input().split())
# 상하좌우((3차원 ver.)
dx = [0, 0, 0, 0, -1, 1] 
dy = [-1, 1, 0, 0, 0, 0] 
dz = [0, 0, -1, 1, 0, 0]

graph = []
for _ in range(H):
    layer = []
    for _ in range(N):
        layer.append(list(map(int, input().split())))
    graph.append(layer)

zero= 0
one = 0
one_pos = []
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0 :
                zero += 1
            elif graph[i][j][k] == 1 : 
                one_pos.append((i, j, k))
                one += 1

if zero == M*N*H :
    print("-1")
elif one == M*N*H :
    print("0")
else: bfs(one, one_pos)