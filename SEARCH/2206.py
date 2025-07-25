# 벽 부수고 이동하기
# 벽을 최대 한개 까지는 부수고 이동 가능
# 왼쪽 위 -> 오른쪽 아래 끝으로 가능 최단 경로 구하기

'''
모든 벽에 대해서 bfs 다 돌려버리면 시간 초과 남
'''

''' 
3차원 배열 사용 (그림으로 이해하면 쉬움) 
    - 0번은 벽 안부숨 (다음에 1로 갈 가능성O) / 1번은 벽 부순 후 (다음에 1로는 절대 못감)
    - 이때 그림으로 이해하기 좋은 입력 예시
        3 6
        010000
        010111
        000110
        정답: 12
        
로직) bfs 딱한번만 돌리기
- 이전에 벽은 부쉈는지, 안부쉈는지를 기록하는 변수와 함께 큐에 저장 (좌표, 1) <- 벽 부숨, (좌표, 0) <- 아직 안부숨 
    - wall = 0 일 때, 
        - 이동할 칸이 0 이면:
            0번 방문기록이 없을 때, 0번 방문기록 = 0번 부모 + 1
        - 이동할 칸이 1 이면:
            1번 방문기록이 없을 때, 1번 방문기록 = 0번 부모 + 1
        - 큐에는 좌표랑 이동할 칸 (0 또는 1) 넣기 

    - wall = 1 이면, 
        - 이동할 칸이 0 이면: 
            1번 방문기록이 없을 때, 1번 방문기록 = 1번 부모 + 1
        - 이동할 칸이 1 이면, 이동 불가
        - 큐에는 좌표랑 1 넣기
'''

from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
board = []
for _ in range(N) : board.append(list(map(int, input().strip())))

def is_inrange(x, y) : 
    return 0<=x<N and 0<=y<M

def bfs() : 
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    que = deque()
    que.append((0, 0, 0))
    visited[0][0][0] = 1

    cnt = 1
    while que : 
        x, y, wall = que.popleft()
        
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if not is_inrange(nx, ny) : continue
            if wall == 0 : 
                if board[nx][ny] == 0 and not visited[nx][ny][0]: 
                    visited[nx][ny][0] = visited[x][y][0] + 1
                    que.append((nx, ny, 0))
                elif board[nx][ny] == 1 and not visited[nx][ny][1]: 
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    que.append((nx, ny, 1))
                
            elif wall == 1 : 
                if board[nx][ny] == 0 and not visited[nx][ny][1]: 
                    visited[nx][ny][1] = visited[x][y][1] + 1
                    que.append((nx, ny, 1))
    
    return visited

visit = bfs()

if visit[N-1][M-1][0] == 0 and visit[N-1][M-1][1] == 0 : print(-1)
elif visit[N-1][M-1][0] == 0 and visit[N-1][M-1][1] != 0 : print(visit[N-1][M-1][1])
elif visit[N-1][M-1][0] != 0 and visit[N-1][M-1][1] == 0 : print(visit[N-1][M-1][0])
else : print(min(visit[N-1][M-1][0], visit[N-1][M-1][1]))