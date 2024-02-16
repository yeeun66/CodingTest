# 토마토
# BFS

# 입력: 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
# 출력: 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 함
# 저장될 때부터 모든 토마토가 익어있는 상태이면 0 출력, 모두 익지는 못하는 상황이면 -1 출력.

# bfs 들어가기 전 while에서는 모두 0, 모두 1 인 경우 먼저 처리 하고
# 초기 1이었던 갯수와 좌표 저장해서 bfs에 넘겨주기
# bfs 에서 one 갯수 만큼 pop 하면 day 카운트 하고 queue 작동은 계속 그대로

import sys
from collections import deque

input = sys.stdin.readline

# 상하좌우
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs(onee, one_poss):
    day = -1
    queue = deque()
    for i in range(onee) :
        x, y = one_poss[i]
        queue.append((x, y))

    while queue : 
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0 :
                graph[nx][ny] = 1
                queue.append((nx, ny))

        onee -= 1
        if onee == 0 :
            day += 1
            onee = len(queue)
    
    for i in range(N): # 모든 작업을 했는데도 0이 남아있는 경우 익을 수 없는 토마토
        for j in range(M):
            if graph[i][j] == 0 :
                print("-1")
                return
    print(day)
            
            
M, N = map(int, input().split())
graph = []
for _ in range(N) :
    graph.append(list(map(int, input().split())))

zero= 0
one = 0
one_pos = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 :
            zero += 1
        elif graph[i][j] == 1 : 
            one_pos.append((i, j))
            one += 1
            
if zero == M*N :
    print("-1")
elif one == M*N :
    print("0")
else: bfs(one, one_pos)