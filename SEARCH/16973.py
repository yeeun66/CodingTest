# 직사각형 탈출

'''
로직 - bfs (시간초과)
1. 상하좌우 이동하는데, 직사각형 전체 같이 움직임
    - 좌표중 하나라도 벽에 걸리거나, 경계 벗어나면 이동 X
    - 큐에는 왼쪽 위 좌표만 넣고, 이동 후 검사할 때만 모든 좌표 검사
2. 직사각형의 왼쪽 위 좌표가 도착좌표가 되면 bfs 종료
3. 이동 불가면 -1 출력 
'''

'''
(시간초과 해결 로직)
모든 경우에 직사각형을 다 검사하면 안됨.
- 오른쪽으로 움직일 경우, 새로운 오른쪽 col만 검사
- 위쪽으로 움직일 경우 새로운 위쪽 row만 검사
.. 이런식으로 해줘야 연산 아낄 수 잇음 
'''

from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
board = []
for _ in range(N) : board.append(list(map(int, input().split())))
H, W, sr, sc, fr, fc = map(int, input().split())
sr, sc, fr, fc = sr-1, sc-1, fr-1, fc-1 

def is_inrange(x, y) :
    return 0<=x<N and 0<=y<M

def check_rect(direct, x, y) :
    if direct == 0 : # 위쪽 - 위 행만 검사
        for j in range(y, y+W) :
            if not is_inrange(x, j) or board[x][j] == 1 : return False
    
    if direct == 1 : # 아래쪽 - 아래 행만 검사
        for j in range(y, y+W) :
            if not is_inrange(x+H-1, j) or board[x+H-1][j] == 1 : return False
    
    if direct == 2 : # 왼쪽, 왼쪽 열만 검사
        for i in range(x, x+H) :
            if not is_inrange(i, y) or board[i][y] == 1 : return False
    
    if direct == 3 : # 오른쪽, 오른쪽 열만 검사
        for i in range(x, x+H) :
            if not is_inrange(i, y+W-1) or board[i][y+W-1] == 1 : return False
    
    return True

def bfs(x, y) :
    visited = [[0 for _ in range(M)] for _ in range(N)]
    que = deque()
    que.append((x, y))
    visited[x][y] = 1

    while que : 
        x, y = que.popleft()
        if (x, y) == (fr, fc) : 
            print(visited[x][y]-1)
            exit()
        for d in range(4) :
            nx, ny = x + dx[d], y + dy[d]
            if is_inrange(nx, ny) and not visited[nx][ny] and not board[nx][ny]: 
                visited[nx][ny] = visited[x][y] + 1
            else : continue

            flag = check_rect(d, nx, ny) # 방향, 왼쪽 위 좌표 
            
            if flag : # 이동 가능할 때 
                que.append((nx, ny))

bfs(sr, sc)
print(-1)