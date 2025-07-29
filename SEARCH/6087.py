# 레이저 통신
'''
로직
bfs로 하나의 C부터 시작해서 다른 C 찾가
이때 거울의 갯수는 가는 길에 방향 바꾼 횟수와 같음

1. 처음 C 두개로 start 좌표와 end 좌표 저장해두기
2. bfs로 최단 거리 구하기
- 큐에 좌표와 cnt, 온 방향까지 저장
- visited 방문 배열과 mirror 거울 배열 함께 관리 

- 방문되어 있지 않으면, 방문 표시하고 아래 조건 검사해서 큐에 매달기
    1) 다음 갈 곳의 방향과 부모의 방향이 같으면 cnt로 주고, mirror에 cnt 저장
    2) 다음 갈 곳의 방향과 부모의 방향이 다르면 cnt + 1 로 줌, mirror에 cnt+1 저장
- 방문되어 있을 때, 
    - mirror의 cnt가 현재 방문했을 때 cnt보다 크면, 현재 방문 cnt로 업데이트 후 큐에 매달기 (다익스트라 개념)
'''
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
M, N = map(int, input().split())
board = []
for _ in range(N) : board.append(list(map(str, input().strip())))

sx, sy, ex, ey = -1, -1, -1, -1
for i in range(N) :
    if (ex, ey) != (-1, -1) : break
    for j in range(M) :
        if board[i][j] == 'C' and (sx, sy) == (-1, -1) : sx, sy = i, j
        elif board[i][j] == 'C' and (sx, sy) != (-1, -1) and (ex, ey) == (-1, -1)  : 
            ex, ey = i, j
            break

def is_inrange(x, y) : 
    return 0<=x<N and 0<=y<M

def bfs(x, y) : 
    visited = [[0 for _ in range(M)] for _ in range(N)]
    mirror = [[0 for _ in range(M)] for _ in range(N)]
    exist = set() # 큐 중복 방지
    que = deque()
    que.append((x, y, -1, 0))
    visited[x][y] = 1

    while que : 
        x, y, d, cnt = que.popleft()
        for i in range(4) : 
            nx, ny = x + dx[i], y + dy[i]
            if is_inrange(nx, ny) and board[nx][ny] != '*' : 
                if not visited[nx][ny] : 
                    visited[nx][ny] = 1
                    tmp_cnt = cnt
                    if d != -1 and d != i: tmp_cnt += 1
                    mirror[nx][ny] = tmp_cnt 
                    que.append((nx, ny, i, tmp_cnt))
                    exist.add((nx, ny, i))
                else : 
                    tmp_cnt = -1
                    if d != -1 and d != i: tmp_cnt = cnt + 1
                    if d != -1 and d == i : tmp_cnt = cnt
                    if mirror[nx][ny] > tmp_cnt : 
                        mirror[nx][ny] = tmp_cnt
                        que.append((nx, ny, i, tmp_cnt))
                    elif mirror[nx][ny] == tmp_cnt : 
                        if (nx, ny, i) not in exist : # 큐 중복 방지 
                            que.append((nx, ny, i, tmp_cnt))
    
    return mirror

min_mirror = bfs(sx, sy)
print(min_mirror[ex][ey])