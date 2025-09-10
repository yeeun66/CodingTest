# 코드트리 - 예술성 

'''
2:30~
로직
total_score: 최종 출력할 (초기 + 1회전 + 2회전 + 3회전) 모두 합친 값 
흐름 <1 -> 2 -> 1 -> 2 -> 1 -> 2 -> 1> 수행 후 total_score 출력
1. 예술 점수 구하기
    score = 해당 턴의 스코어 
    (1) 그룹 나누기 
        - 상하좌우 인접한 동일 숫자 그룹 
        - 각 group에 해당하는 칸의 모든 좌표 저장 (bfs)
    (2) 조화로움 계산 
        - 1번 그룹부터 k번 그룹까지 모든 다른 그룹과의 조화로움 계산에서 score에 더하기
        - 조화로움 = (a그룹 칸의수 + b그룹 칸의 수) * 그룹a의 값 * 그룹 b의 값 * a~b가 맞닿아 있는 변의 수
            - a~b가 맞닿아 있는 변의 수 구하기:
                -a의 모든 좌표에 대해, 상하좌우로 움직인 좌표가 b에 들어있다면, 변의수 += 1

2. 회전하기
    동시 회전이니까 새로운 배열에 덮어쓰고 변경 후 리턴
    (1) 십자모양 반시계 90도 회전 
        가운데 세로 => for i in range(n) : new[n//2][i] = old[i][n//2]
        가운데 가로 => for i in range(n) : new[n-1-i][n//2] = old[n//2][i]
    (2) 나머지 사각형 4개 시계 90도 회전
        임시 (n//2 * n//2) 크기의 사각형 만들어줌 
        거기서 절대좌표 -> 상대좌표 -> 회전 -> 절대좌표 과정으로 회전

        상대좌표 회전 -> new[i][j] = old[j][n//2-1-i]
'''

from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
board = []
for _ in range(n) : board.append(list(map(int, input().split())))

def is_inrange(x, y) : 
    return 0<=x<n and 0<=y<n

def bfs(x, y, visited) : 
    que = deque()
    group = []
    que.append((x, y))
    group.append((x, y))
    value = board[x][y]

    while que : 
        x, y = que.popleft()
        for i in range(4) : 
            nx, ny = x + dx[i], y + dy[i]
            if is_inrange(nx, ny) and not visited[nx][ny] and board[nx][ny] == value : 
                visited[nx][ny] = 1
                que.append((nx, ny))
                group.append((nx, ny))
    
    return group, visited

def calculate_art_score() : 
    score = 0
    group = []
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n) : 
        for j in range(n) : 
            if not visited[i][j] : 
                visited[i][j] = 1
                tmp_group, visited = bfs(i, j, visited)
                group.append(tmp_group)

    group_cnt = len(group) # 그룹 갯수
    for i in range(group_cnt) : 
        for j in range(i+1, group_cnt) : 
            # a~b가 맞닿아 있는 변의 수 구하기 
            num = 0
            for x, y in group[i] : 
                for k in range(4) : 
                    nx, ny = x + dx[k], y + dy[k]
                    if is_inrange(nx, ny) and (nx, ny) in group[j] :
                        num += 1

            if num == 0 : continue
            temp = (len(group[i]) + len(group[j])) * board[group[i][0][0]][group[i][0][1]] *  board[group[j][0][0]][group[j][0][1]] * num
            score += temp

    return score

def rotate_board() : 
    new_board = [b[:] for b in board]
    # 십자회전
    for i in range(n) : new_board[n//2][i] = board[i][n//2]
    for i in range(n) : new_board[n-1-i][n//2] = board[n//2][i]

    # 정사각형 4개
    # 좌상단 -> 그대로
    for i in range(n//2) : 
        for j in range(n//2) : 
            new_board[j][n//2-1-i] = board[i][j]
    # 우상단 -> 행 그대로, 열만 상대좌표 변환
    tmp_rect = [[0 for _ in range(n//2)] for _ in range(n//2)]
    for i in range(n//2) : 
        for j in range(n//2+1, n) : 
            si, sj = i, j - (n//2 + 1) # 절대 -> 상대
            tmp_rect[si][sj] = board[i][j]
    
    new_rect = [r[:] for r in tmp_rect]
    for i in range(n//2) : 
        for j in range(n//2) : 
            new_rect[j][n//2-1-i] = tmp_rect[i][j]
    # 상대 -> 절대 
    for i in range(n//2) : 
        for j in range(n//2) : 
            si, sj = i, j + (n//2 + 1)
            new_board[si][sj] = new_rect[i][j]
    
    # 좌하단 -> 행 상대좌표 변환, 열 그대로 
    tmp_rect = [[0 for _ in range(n//2)] for _ in range(n//2)]
    for i in range(n//2+1, n) : 
        for j in range(n//2) : 
            si, sj = i - (n//2 + 1) , j#  절대 -> 상대
            tmp_rect[si][sj] = board[i][j]
    
    new_rect = [r[:] for r in tmp_rect]
    for i in range(n//2) : 
        for j in range(n//2) : 
            new_rect[j][n//2-1-i] = tmp_rect[i][j] # 작은 사각형 회전
    
    # 상대 -> 절대 
    for i in range(n//2) : 
        for j in range(n//2) : 
            si, sj = i + (n//2 + 1), j
            new_board[si][sj] = new_rect[i][j]
    
    # 우하단 -> 행 열 모두 상대좌표 변환
    tmp_rect = [[0 for _ in range(n//2)] for _ in range(n//2)]
    for i in range(n//2+1, n) : 
        for j in range(n//2+1, n) : 
            si, sj = i - (n//2 + 1) , j - (n//2 + 1)#  절대 -> 상대
            tmp_rect[si][sj] = board[i][j]
    
    new_rect = [r[:] for r in tmp_rect]
    for i in range(n//2) : 
        for j in range(n//2) : 
            new_rect[j][n//2-1-i] = tmp_rect[i][j] # 작은 사각형 회전
    
    # 상대 -> 절대 
    for i in range(n//2) : 
        for j in range(n//2) : 
            si, sj = i + (n//2 + 1), j + (n//2 + 1)
            new_board[si][sj] = new_rect[i][j]

    return new_board

total_score = 0
total_score += calculate_art_score() # 초기 점수

for _ in range(3) : # 3번 더 반복
    board = rotate_board()
    total_score += calculate_art_score()

print(total_score)
