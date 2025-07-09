# 경쟁적 전염

# 시험관 좌상단 (1,1) -> (0,0)으로 바꿔서 생각 

"""
로직
0. 시험관 배열 관리
    - N * N 크기의 2차원 배열
    - 빈칸은 0으로 두기
1. 1~K 번호 순서대로 상하좌우로 1초마다 바이스러스 증식 (bfs-큐 사용)
    - 이때 0인 칸에만 증식 가능
    - 한 종류의 바이러스 증식 후에 배열 업데이트 해줘야 함

시간 초과 - 3중 반복문 돌려서 그런듯
>> 시뮬레이션의 우선 순위 로직 처럼, 큐에 바이러스 정보 (번호, 시간, 좌표, 좌표) 넣어서 오름 차순 정렬 후 BFS 수행
그러면 낮은 번호부터 증식 가능하게 됨
"""
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, K = map(int, input().split())
board = []
for _ in range(N) : board.append(list(map(int, input().split())))
S, X, Y = map(int, input().split())

info = [] # 바이러스 정보
for i in range(N) :
    for j in range(N) :
        if board[i][j] != 0 :
            info.append([board[i][j], 0, i, j])
info.sort() 

def is_inrange(x, y) :
    return 0 <= x < N and 0 <= y < N

def bfs():
    visited = [[0 for _ in range(N)] for _ in range(N)]
    que = deque(info)

    while que : 
        num, sec, x, y = que.popleft()
        if sec == S : break # 시간 끝나면 종료
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if is_inrange(nx, ny) and not visited[nx][ny] :
                if board[nx][ny] == 0 : 
                    board[nx][ny] = num
                    que.append([num, sec+1, nx, ny])
                else : continue
                visited[nx][ny] = 1

    return board

board = bfs()

print(board[X-1][Y-1])