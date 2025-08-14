# 원판 돌리기
'''
로직
1. 원판으로 인접 영역 설계
    - 그냥 그대로 입력 받되, 
        - 같은 원판에서는 0번째와 M-1 번째도 연결 되어있다고 가정
        - 다른 원판에서는 같은 열에서 한칸 차이면 연결되어 있다고 가정   
    - 0번째는 모두 0으로 M개 채워 두기  

아래를 T번 반복
2. 원판 돌리기
    - 번호가 x의 배수인 원판을 d방향 (0:시계, 1:반시계)으로 k칸 회전 시킴 
    - 행을 기준으로 회전이니까, 배열 슬라이싱으로 수행
        - 시계 방향 이면, 끝에꺼 k개 떼서 앞에 순서대로 붙이기
        - 반시계 방향이면, 앞에 k개 떼서 뒤에 순서대로 붙이기
3. 숫자 조정
    - 원판에 수가 남아있을 때, - exist_num
        - 인접하면서 수가 같은 것이 있으면, 그 수는 모두 0으로 만든다
        - 위 같은 수가 없으면, 
            원판의 적힌 수의 평균 구해서, 평균 보다 크면 -=1, 평균보다 작으면 +=1 해준다
        - 이때 (0, 즉 없어진 것 제외)

4. 원판에 남아있는 숫자 합 출력 
'''

import sys; input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 

N, M, T = map(int, input().split())
board = [] # 원판 보드
tmp = []
for _ in range(M) : tmp.append(0)
board.append(tmp)
for _ in range(N) : board.append(list(map(int, input().split())))
cmd = [] # t번 수행해야할 회전
for _ in range(T) : cmd.append(list(map(int, input().split())))

def rotate(idx, di, kk) :
    if di == 0 : # 시계
        board[idx] = board[idx][M-kk:] + board[idx][0:M-kk]
    else : # 반시계
        board[idx] = board[idx][kk:] + board[idx][0:kk]

def exist_num() : 
    for i in range(1, N+1) : 
        for j in range(M) : 
            if board[i][j] != 0 : return True
    
    return False

def neighbor() : 
    # 바로 0으로 바꾸지 말고, 좌표(i, j)로 저장 해뒀다가 마지막에 바꾸기
    find = set()
    for i in range(1, N+1) : 
        for j in range(M) : 
            cur = board[i][j]
            if cur == 0 : continue
            for k in range(4) :
                nx, ny = i + dx[k], j + dy[k]
                if ny == -1 : ny = M-1
                elif ny == M : ny = 0
                if nx == -1 or nx == N+1 : continue 
                if board[nx][ny] == cur : 
                    if (i, j) not in find : find.add((i, j))
                    if (nx, ny) not in find : find.add((nx, ny))

    if not find : return False
    else : 
        for x, y in find : 
            board[x][y] = 0
        return True

def avgs() : 
    cnt = 0
    sums = 0
    for i in range(1, N+1) : 
        for j in range(M) : 
            if board[i][j] != 0 : 
                cnt += 1
                sums += board[i][j]
    
    average = sums / cnt 
    for i in range(1, N+1) : 
        for j in range(M) : 
            if board[i][j] != 0 :
                if board[i][j] > average : board[i][j] -= 1
                elif board[i][j] < average: board[i][j] += 1


for t in range(T) : 
    x, d, k = cmd[t] 

    for i in range(1, N+1) : # 2. 원판 회전
        if i % x == 0 : rotate(i, d, k) 
    
    if exist_num() : # 3. 숫자 조정 
        if not neighbor() : 
            avgs() # 평균 구해서 조정

    else : # 조기 종료
        print(0)
        exit()
    
sums = 0
for b in board: 
    sums += sum(b)
print(sums)
