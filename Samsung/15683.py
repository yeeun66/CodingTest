# 감시 (완전탐색)
# CCTV의 방향을 적절히 정해서, 사각 지대의 최소 크기를 구하는 프로그램을 작성
'''
로직
1번 CCTV: 한방향 탐색 (총 4가지 가능)
2번 CCTV: 서로 반대인 두 방향 탐색 (총 2가지 가능)
3번 CCTV: 서로 직각인 두 방향 탐색 (총 4가지 가능)
4번 CCTV: 세 방향 탐색 (총 4가지 가능)
5번 CCTV: 네 방향 탐색 (총 1가지 가능)

1. 현재 격자에 있는 CCTV 종류에 따라 모든 경우의 수 만들기 (진법 완탐 활용)
    - 변수들이 가질 수 있는 값이 여러 개이고 모든 조합을 다 확인해보고 싶은데 변수들끼리는 독립적일 땐 
        -> 백트래킹 보다 '진법'을 이용한 방법이 더 쉬운 방법이라고 함
    각 경우에 대해서 cctv_search 함수로 현재 케이스 보드 업데이트 
    
2. 각 경우마다 CCTV 탐색 해서 사각지대 수 구하기 - cctv_search
    - 각 CCTV에 대해 해당 방향으로 모두 탐색 -> 탐색한 빈칸은 # 으로 만들기
    - 경계 밖이거나 6을 만날 때 까지 계속 탐색
    
3. 현재 케이스 보드에서 남은 0 (사각지대)의 수 구해서 현재 최소 사각지대 수와 비교 후 업데이트

4. 최소 사각지대 수 리턴
'''

from collections import deque
import sys; input = sys.stdin.readline
dx = [-1, 0, 1, 0] # 상우하좌
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
board = []
for _ in range(N) : board.append(list(map(int, input().split())))
cctv = []
for i in range(N) : 
    for j in range(M) : 
        if 0 < board[i][j] < 6 : 
            cctv.append((board[i][j], i, j)) # cctv 번호, 좌표

def is_inrange(x, y) : 
    return 0<=x<N and 0<=y<M 

def cctv_search(x, y, d) :
    
    nx, ny = x + dx[d], y + dy[d]
    while is_inrange(nx, ny) and new_board[nx][ny] != 6 : 
        if new_board[nx][ny] == 0 : new_board[nx][ny] = '#'
        nx, ny = nx + dx[d], ny + dy[d]

    
min_area = N * M + 1
for i in range(4**len(cctv)) : # i가 하나의 케이스. ex) cctv가 3개면 총 64개의 케이스 존재
    new_board = [b[:] for b in board]
    case = i
    for j in range(len(cctv)) :
        direct = case % 4 # 현재 j가 가질 방향 (0~4)
        case //= 4 # 다음 자리로 넘어가기

        num, x, y = cctv[j]
        if num == 1 : 
            cctv_search(x, y, direct)
        elif num == 2 : 
            cctv_search(x, y, direct); cctv_search(x, y, (direct+2)%4)
        elif num == 3 : 
            cctv_search(x, y, direct); cctv_search(x, y, (direct+1)%4)
        elif num == 4 : 
            cctv_search(x, y, direct); cctv_search(x, y, (direct+1)%4); cctv_search(x, y, (direct+2)%4)
        elif num == 5 : 
            cctv_search(x, y, direct); cctv_search(x, y, (direct+1)%4); cctv_search(x, y, (direct+2)%4); cctv_search(x, y, (direct+3)%4)

    tmp_zero = 0
    for new in new_board : 
        tmp_zero += new.count(0)
    
    min_area = min(min_area, tmp_zero)
    
print(min_area)
