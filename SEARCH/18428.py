# 감시 피하기

"""
로직
장애물 3개 놓는 모든 경우에 대해 감시 피할 수 있는지 여부 확인
1. 장애물 3개 모든 위치 경우의 수 구하기. (x, y) 쌍 3개 - backtrack 
    - block = [(x1, y1), (x2, y2), (x3, y3)]
    - possible 함수에 block 배열 넘겨 주기

2. 각 경우에 대해 감시 피할 수 있는지 여부 확인 - possible
    1. check 함수에 block 배열 넘겨 주기
    2. check 함수에서 한번이라도 Fasle 받으면 (즉 감시 당하면) 바로 이 경우는 끝. 리턴
        - 단 한번도 감시 받지 않으면, 이 경우는 감시 피할 수 있는 방법. 바로 YES 출력 후 프로그램 종료

3. 감시 피했는지 확인 - check
    1. board에 block(장애물) O로 설치하기 
    2. 모든 선생님들이 상하좌우로 모든 학생 탐색 
        - 상하좌우만 탐색 가능. 중간에 O를 마주치면 해당 방향으로는 탐색 종료
        - 탐색 종료전 학생(S)을 만나면 False를 리턴
    3. 탐색 종료 후에도 리턴 안되었다면, True리턴

4. 프로그램 완전 종료
    - 모든 프로그램에 대해 아직 종료 안되었다면, NO 출력 후, 프로그램 종료
"""
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
board = []
for _ in range(N) : board.append(list(map(str, input().split())))

# 선생님 좌표 미리 담아두기
teacher = []
for i in range(N) :
    for j in range(N) :
        if board[i][j] == 'T' :
            teacher.append((i, j))

def is_inrange(x, y) :
    return 0 <= x < N and 0 <= y < N 

def check(blk) :
    test_board = [b[:] for b in board]
    for (x, y) in blk : test_board[x][y] = 'O'
    
    for (x, y) in teacher :
        for i in range(4) :
            n = 1
            nx, ny = x + n*dx[i], y + n*dy[i]
            
            while is_inrange(nx, ny) :
                if test_board[nx][ny] == 'O' : break
                if test_board[nx][ny] == 'S' : return False
                n += 1
                nx, ny = x + n*dx[i], y + n*dy[i]
    
    return True

def possible(b) :
    cond = check(b)
    if cond == False : return
    else : 
        print('YES')
        exit()

def backtrack() :
    if len(block) == 3 : 
        possible(block)
        return
    
    for i in range(N) :
        for j in range(N) :
            if (i, j) in block : continue # 중복은 안됨
            if board[i][j] == 'X' : # 빈칸만 차지 가능
                block.append((i, j))
                backtrack()
                block.pop()

block = []
backtrack()

print('NO')