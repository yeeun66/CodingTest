'''
4:00

0. 배열 관리 
    - board 값 (벽:-1, 0: 빈칸, 양수: 나무)
    - trees: 현재 살아있는 나무들이 있는 칸의 정보 (좌표, 나무 수) 
    - remover_board: 제초제만 따로 관리하는 보드 (양수: 제초제 존재, 0: 제초제 없음)

아래를 m번 반복

1. 제초제 -=1
    - remover_board 양수이면 -= 1

2. 나무 성장 (동시 성장)
    - 각 나무에 대해 인접 네칸 중 나무 있는 수만큼 성장
    - 각 tree의 좌표에서 인접 칸 나무 수 카운트
    - 그만큼 성장 후 trees에 업데이트 
    - board에도 업데이트 

3. 나무 번식 (동시 번식)
    - new_board를 board 복사해서 생성
    - 기존 나무들은 인접 네칸 중 빈칸에 번식함 (벽, 나무, 제초제 모두 없어야 함)
    - 이때 각 칸에 번식하는 나무 수(= 부모 // 번식가능칸)를 new_board에 더해주기 
    - 이때 새로운 나무들도 trees에 추가해줘야 함 (완성된 new_board 이중 for문으로 집어넣기)
    - new_board 리턴 

4. 제초제 뿌리기
    - 각 칸 중 제초제 뿌렸을 때 가장 많은 나무가 박멸되는 칸에 제초제 뿌림
    1) trees 오름차순 솔팅 후 아래 진행 (행작열작)
    2) 각 좌표에 대해 그 좌표에 제초제 뿌렸다 가정하고 박멸 나무 수 구하기 (dead_cnt)
        - removing() 함수에서 진행. dead_cnt
        - 해당 칸부터 4방향 대각선으로 bfs 진행 depth는 k만큼
            - 이때 나무 없는 칸이면, 큐에 추가X
            - 나무 있는 칸이면 dead_cnt에 그루 수 추가 
        dead_cnt가 현재 max_dead 보다 크다면, 좌표랑 max_dead 업데이트
    3) 최종 확정된 좌표로 제초작업 수행
        - 아까 removing() 활용해서 real_removing() 만들어 호출
            - 이때는 보드랑 트리에 업데이트 반영
                - 죽은 나무 제외하고 살아남은 나무만 trees랑 board에 다시 업데이트 
                - remover_board에 제초제(c) 뿌리기 

5. 박멸한 나무 수 구해서 result에 더하기 
'''
# 시간초과 해결 : tree 다 죽으면 강제종료해서 해결
# 맞았긴한데 다른 사람에 비해 실행시간이 좀 길다 -> 더 빠르게 코드 다시 짜보기 
    # 일단 쓸데없는 visited 다 줄여서 100ms 줄이긴 함

from collections import deque
dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]
cx = [-1, -1, 1, 1] # 대각선 4방향
cy = [-1, 1, -1, 1] 

n, m, k, c = map(int, input().split())
board = []
for _ in range(n) : board.append(list(map(int, input().split())))
remover_board = [[0 for _ in range(n)] for _ in range(n)]
trees = []
for i in range(n) : 
    for j in range(n) : 
        if board[i][j] > 0 : trees.append((i, j, board[i][j])) # 나무 좌표, 나무 갯수

def is_inrange(x, y) :
    return 0<=x<n and 0<=y<n 

def grow_tree() : 
    for i in range(len(trees)) :
        x, y, num = trees[i] 
        cnt = 0
        for d in range(4) : 
            nx, ny = x + dx[d], y + dy[d]
            if is_inrange(nx, ny) and board[nx][ny] > 0 : cnt += 1
        
        trees[i] = (x, y, num+cnt)
        board[x][y] = num + cnt

def make_tree() : 
    new_board = [b[:] for b in board] 
    for x, y, num in trees : 
        cnt = 0
        babies = []
        for i in range(4) : 
            nx, ny = x + dx[i], y + dy[i]
            if is_inrange(nx, ny) and board[nx][ny] == 0 and remover_board[nx][ny] == 0 : 
                cnt += 1
                babies.append((nx, ny))
        if cnt == 0 : continue
        number = num // cnt 
        for nx, ny in babies : new_board[nx][ny] += number 
    
    for i in range(n) :
        for j in range(n) : 
            if new_board[i][j] > 0 and (i, j, new_board[i][j]) not in trees : 
                trees.append((i, j, new_board[i][j]))
    
    return new_board


def removing(x, y) : 
    dead_cnt = board[x][y]
    que = deque() 
    que.append((x, y, 0, -1)) # 4번째 값은 전파 방향 -> 즉 처음은 네방향 가능인데 나중은 본인 방향으로만 가능

    while que : 
        x, y, depth, direct = que.popleft()
        if depth == k : continue
        if direct == -1 : 
            for i in range(4) : 
                nx, ny = x + cx[i], y + cy[i]
                if is_inrange(nx, ny) and board[nx][ny] > 0 : 
                    que.append((nx, ny, depth+1, i))
                    dead_cnt += board[nx][ny]
        else : 
            nx, ny = x + cx[direct], y + cy[direct]
            if is_inrange(nx, ny) and board[nx][ny] > 0 : 
                que.append((nx, ny, depth+1, direct))
                dead_cnt += board[nx][ny]

    return dead_cnt

def real_removing(x, y) : 
    dead_cnt = board[x][y]
    que = deque() 
    que.append((x, y, 0, -1)) # 4번째 값은 전파 방향 -> 즉 처음은 네방향 가능인데 나중은 본인 방향으로만 가능
    remover_board[x][y] = c+1
    dead_trees = set()
    dead_trees.add((x, y))

    while que : 
        x, y, depth, direct = que.popleft()
        if depth == k : continue
        if direct == -1 : 
            for i in range(4) : 
                nx, ny = x + cx[i], y + cy[i]
                if is_inrange(nx, ny) : 
                    if board[nx][ny] > 0 : 
                        que.append((nx, ny, depth+1, i))
                        dead_cnt += board[nx][ny]
                        remover_board[nx][ny] = c+1
                        dead_trees.add((nx, ny))
                    else : 
                        remover_board[nx][ny] = c+1
        else : 
            nx, ny = x + cx[direct], y + cy[direct]
            if is_inrange(nx, ny) : 
                if board[nx][ny] > 0 : 
                    que.append((nx, ny, depth+1, direct))
                    dead_cnt += board[nx][ny]
                    remover_board[nx][ny] = c+1
                    dead_trees.add((nx, ny))
                else : 
                    remover_board[nx][ny] = c+1
    
    new_trees = []
    for x, y, num in trees : 
        if (x, y) in dead_trees : board[x][y] = 0
        else : new_trees.append((x, y, num))

    return dead_cnt, new_trees

def remove_tree() : 
    trees.sort()
    max_dead = 0
    fx, fy = -1, -1
    for x, y, _ in trees : 
        dead_cnt = removing(x, y)
        if dead_cnt > max_dead : 
            max_dead = dead_cnt
            fx, fy = x, y
    
    if (fx, fy) == (-1, -1) : return 0, []
    return real_removing(fx, fy)

result = 0
for turn in range(m) : 
    if not trees : break 
    # 1
    for i in range(n) : 
        for j in range(n) : 
            if remover_board[i][j] > 0 : remover_board[i][j] -= 1
    
    grow_tree() # 2
    board = make_tree() # 3
    dead_tree_cnt, trees = remove_tree() # 4
    result += dead_tree_cnt # 5

print(result)