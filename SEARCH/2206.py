# 벽 부수고 이동하기
# 최단거리 이동 - 벽 1개까지 부수기 가능

"""
(시간초과 로직 - 모든 벽에 대해서 bfs 다 돌려버리기)
1. 처음에 벽 안부수는 최단 거리 계산(bfs) - min_dist에 넣어두기
2. 벽을 한개씩 없애서(그냥 반복문) 최단거리 탐색(bfs)
    - 각 경우에 대해 현재 min_dist보다 작으면, 그 값으로 업데이트
3. 이동 불가하면, 즉 첫 min_dist가 여전히 무한대면, -1 출력
"""

"""
(시간초과 해결- 3차원 배열 아이디어)
아이디어: 0번째 2차원 방문 벽을 안부수는 방문 / 1번째 2차원 방문은 벽을 부순 후 방문
- 큐에 (좌표, 벽 부서져서 온 것인지 여부를 나타냄 brk 1이면 부서져서 온 것)
- 벽 부서져서 온 것은 다음에 새로운 벽 더이상 부술 수 X
- 벽 아직 안부수고 큐에 담긴 건 다음에 1을 만나면 벽 부술 수 있음

"""
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
board = []
for _ in range(N) : board.append(list(map(int, input().strip())))
board[N-1][M-1] = 2 # 도착 지점 
INF = 1000000
min_dist = INF

def is_inrange(x, y) :
    return 0<=x<N and 0<=y<M

def bfs() :
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    # for v in visited : print(v)
    visited[0][0][0] = 1
    que = deque()
    que.append((0, 0))
    while que : 
        x, y = que.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if is_inrange(nx, ny) and not visited[nx][ny] and board[nx][ny] != 1:
                if board[nx][ny] == 2 : return visited[x][y] + 1
                visited[nx][ny] = visited[x][y] + 1
                que.append((nx, ny))
    
    return INF

min_dist = bfs() # 1

for i in range(N) :
    for j in range(M) :
        if board[i][j] == 1 : 
            board[i][j] = 0
            temp = bfs() # 2
            min_dist = min(min_dist, temp)
            board[i][j] = 1

if min_dist == INF : print(-1) # 3
else : print(min_dist)
