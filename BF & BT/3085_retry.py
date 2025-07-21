# 사탕 게임 - 완전탐색 

'''
일단 먹을 수 있는 최대 갯수는 N개
바꿀 수 있는 좌표 2개를 선택하며 (모두 선택되어 수행될때까지) 아래를 반복 - backtrack

0. 원본 배열은 건들이지 말 것
1. 인접하고 색이 서로 다른 두 위치를 선택 후, 두 칸의 위치를 서로 바꾼다
2. 바꾼 배열로 먹을 수 있는 사탕의 최대 갯수 구한다 - bfs는 굳이 안써도 되고 그냥 구현 
3. 바꾼 위치 원상복귀 (이건 걍 board에 되어있으니까 안해도 상관 없음)
'''
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
board = []
swap = set() # 교환 했던 좌표 
max_candy = 0 # 최대 사탕 수 

for _ in range(N) : board.append(list(map(str, input().strip())))

def is_inrange(x, y) :
    return 0<=x<N and 0<=y<N

def find_max():
    final_cnt = 0 
    # row 먼저 카운트 
    for i in range(N) :
        tmp_cnt = 1
        j = 0
        cur = new_board[i][j]
        nx, ny = i, j+1
        while True : 
            if not is_inrange(nx, ny) : # 경계 벗어날 때도 이때까지 값 업데이트 해줌
                final_cnt = max(final_cnt, tmp_cnt)
                break
            if new_board[nx][ny] == cur : # 다음 값이 현재 값이랑 같으면 계속 찾아
                tmp_cnt += 1
                nx, ny = nx, ny+1
            else : # 색 다르면, 이때까지 값 업데이트 하고, 색도 다른걸로 업데이트 하고 계속 찾아  
                final_cnt = max(final_cnt, tmp_cnt)
                tmp_cnt = 1
                cur = new_board[nx][ny]
                nx, ny = nx, ny+1
    
    # 이제 세로 카운트 
    for j in range(N) :
        tmp_cnt = 1
        i = 0
        cur = new_board[i][j]
        nx, ny = i+1, j
        while True : 
            if not is_inrange(nx, ny) : 
                final_cnt = max(final_cnt, tmp_cnt)
                break
            if new_board[nx][ny] == cur : # 다음 값이 현재 값이랑 같으면 계속 찾아
                tmp_cnt += 1
                nx, ny = nx+1, ny
            else : # 색 다르면, 이때까지 값 업데이트 하고, 색도 다른걸로 업데이트 하고 계속 찾아  
                final_cnt = max(final_cnt, tmp_cnt)
                tmp_cnt = 1
                cur = new_board[nx][ny]
                nx, ny = nx+1, ny
    
    return final_cnt

#### Main ####
for x in range(N) :
    for y in range(N) :
        color1 = board[x][y]
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if is_inrange(nx, ny) and color1 != board[nx][ny] and (x, y, nx, ny) not in swap : 
                swap.add((x, y, nx, ny))
                swap.add((nx, ny, x, y))
                new_board = [b[:] for b in board] # 깊은 복사 
                new_board[nx][ny] = color1
                new_board[x][y] = board[nx][ny] # 교환 
                
                tmp_candy = find_max()
                max_candy = max(max_candy, tmp_candy)
                if max_candy == N : 
                    print(N)
                    exit()

print(max_candy)