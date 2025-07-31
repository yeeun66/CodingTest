# 두 동전
# 두 동전 중 하나만 보드에서 떨어뜨리기 위해 버튼을 최소 몇번 눌러야 하는지 구하기
'''
로직
큐에 두 동전에 좌표와 현재 depth 넣기 (r1, c1, r2, c2, 0)
큐 엠티까지 다음을 반복
상하좌우 탐색하며, 
    - 두 동전 모두 이동 불가이면, 즉 둘다 벽을 만나거나 둘다 경계 밖이면 컨티뉴
    - 하나만 이동 가능일 때, 
        - 하나는 빈칸이거나 벽이고, 나머지 하나는 경계 밖이면 depth+1 출력 후 종료
    - 둘다 이동 가능일 때, 즉 둘다 빈칸(.)으로 이동이면 이동 후 좌표 큐에 추가
    - 하나만 이동 가능일 때, 
        - 하나는 빈칸, 하나는 벽으로 이동이면, 빈칸으로 이동하는 좌표만 이동시켜 큐에 추가

    - 종료조건: depth > 10 이 되면 -1 출력 후 종료
큐 엠티라 밖에 나왔을 때도 -1 출력 해줘야 함 
'''

from collections import deque
import sys; input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
board = []
for _ in range(N) : board.append(list(map(str, input().strip())))

r1, c1, r2, c2 = -1, -1, -1, -1
for i in range(N) : 
    for j in range(M) :
        if board[i][j] == 'o' and (r1, c1) == (-1, -1): 
            r1, c1 = i, j 
            board[i][j] = '.'
        if board[i][j] == 'o' and (r1, c1) != (-1, -1): 
            r2, c2 = i, j 
            board[i][j] = '.'
            break

def is_inrange(x, y) : 
    return 0<=x<N and 0<=y<M

visit = set()
que = deque()
que.append((r1, c1, r2, c2, 0))
visit.add((r1, c1, r2, c2))
while que : 
    
    r1, c1, r2, c2, depth = que.popleft()
    if (r1, c1) == (r2, c2) : continue
    if depth >= 10 : 
        print(-1)
        exit()

    for i in range(4) : 
        nr1, nc1, nr2, nc2 = r1 + dx[i], c1+dy[i], r2+dx[i], c2+dy[i]
        if (nr1, nc1, nr2, nc2) in visit : continue
        if not is_inrange(nr1, nc1) and not is_inrange(nr2, nc2) : continue
        if not is_inrange(nr1, nc1) and is_inrange(nr2, nc2) and (board[nr2][nc2] == '#' or board[nr2][nc2] == '.') : 
            print(depth+1)
            exit()
        if not is_inrange(nr2, nc2) and is_inrange(nr1, nc1) and (board[nr1][nc1] == '#' or board[nr1][nc1] == '.') : 
            print(depth+1)
            exit()
        
        if is_inrange(nr1, nc1) and is_inrange(nr2, nc2) : 
            if board[nr1][nc1] == '.' and board[nr2][nc2] == '.': 
                que.append((nr1, nc1, nr2, nc2, depth+1))
                visit.add((nr1, nc1, nr2, nc2))
            elif board[nr1][nc1] == '.' and board[nr2][nc2] == '#' : 
                que.append((nr1, nc1, r2, c2, depth+1))
                visit.add((nr1, nc1, nr2, nc2))
            elif board[nr1][nc1] == '#' and board[nr2][nc2] == '.' : 
                que.append((r1, c1, nr2, nc2, depth+1))
                visit.add((nr1, nc1, nr2, nc2))

print(-1)