# 벽 부수고 이동하기 2
# 벽을 최대 K개 까지 부수고 이동 가능
# 왼쪽 위 -> 오른쪽 아래 끝으로 가능 최단 경로 구하기

''' 
        
로직) 원래 벽 부수고 이동하기(2206) 에서 약간 수정하면됨
(수정 방안) 
visited를 K개의 layer로 관리하기
    - 0번째 layer : 아직 벽 안 부숨
    - 1번째 layer : 벽 1개 부숨
    - k번째 layer : 벽 k개 부숨 - 이제 더 이상 벽 못 부숨
    
(전체 로직)
bfs 딱한번만 돌리기
- 벽 부순 갯수를 기록하는 변수와 함께 큐에 저장 (좌표, wall) 
    - 0 <= wall < k 일 때, 
        - 이동할 칸이 0 이면:
            wall번 방문기록이 없을 때, wall번 방문기록 = wall번 부모 + 1
        - 이동할 칸이 1 이면:
            wall+1 번 방문기록이 없을 때, wall + 1번 방문기록 = wall 번 부모 + 1
            wall += 1
        - 큐에는 좌표랑 wall 넣기 

    - wall == k 이면, 
        - 이동할 칸이 0 이면: 
            wall 번 방문기록이 없을 때, wall번 방문기록 = wall번 부모 + 1
            큐에는 좌표랑 wall 넣기
        - 이동할 칸이 1 이면, 이동 불가
'''
import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M, K = map(int, input().split())
board = []
for _ in range(N) : board.append(list(map(int, input().strip())))

def is_inrange(x, y) : 
    return 0<=x<N and 0<=y<M

def bfs() : 
    visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
    que = deque()
    que.append((0, 0, 0))
    visited[0][0][0] = 1

    while que : 
        x, y, wall = que.popleft()
        
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if not is_inrange(nx, ny) : continue
            if 0 <= wall < K : 
                if board[nx][ny] == 0 and not visited[nx][ny][wall]: 
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    que.append((nx, ny, wall))
                elif board[nx][ny] == 1 and not visited[nx][ny][wall+1]: 
                    visited[nx][ny][wall+1] = visited[x][y][wall] + 1
                    que.append((nx, ny, wall+1))
                
            elif wall == K : 
                if board[nx][ny] == 0 and not visited[nx][ny][wall]: 
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    que.append((nx, ny, wall))
    
    return visited

visit = bfs()

min_dist = N ** 3
for i in range(K+1) : 
    if visit[N-1][M-1][i] != 0 :
        min_dist = min(min_dist, visit[N-1][M-1][i])

if N == 1 and M == 1 : print(1)
elif min_dist == N ** 3 : print(-1)
else : print(min_dist)