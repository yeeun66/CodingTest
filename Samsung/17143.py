# 낚시왕 
# 1시간 
'''
로직
아래 1~3을 C번 반복
0. 상어 정보는 따로 관리 (좌표, 속력, 방향, 크기)
    - 방향 1~4: 상하우좌 
    - 같은 크기를 갖는 상어는 없다고 했으므로, 크기로 상어 고유성 판단 (죽은 상어 판단시에도)
1. 낚시왕 오른쪽으로 한칸 이동 _ 현재 초와 같음 (굳이 이동X)
2. 상어 낚시
    - 현재 열에 있는 상어 중에서 행이 가장 작은 상어 잡는다. 
        - 잡힌 상어는 격자에서 사라짐
        - 잡은 상어의 크기 더해주기 (result)
    - 죽은 상어 배열에 추가 (상어 크기)

3. 상어 이동 
    - 죽은 상어가 아니면, 이동해서 새로운 정보 배열에 추가
    - 주어진 속도로 상어 이동 (상어 정보 업데이트)
    - 격자 경계 넘는 경우에는 방향 반대로 바꿔서 속력 유지한 채로 이동 
    - 같은 칸에 상어 두 마리 이상 있으면, 가장 큰 상어가 다 잡아먹음 
        - 정보 배열 내림차순 솔팅 후, 이미 한번 나왔던 좌표이면, 해당 크기 다 죽은 상어 배열에 추가 (잡아먹힘 처리) 

4. result 출력
'''

from collections import deque
import sys; input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

R, C, M = map(int, input().split())
board = [[0 for _ in range(C)] for _ in range(R)]
shark_info = []
for _ in range(M) : 
    r, c, s, d, z = map(int, input().split())
    shark_info.append((r-1, c-1, z, s, d-1))
    board[r-1][c-1] = z
dead_shark = set() # 죽은 상어의 크기 관리
result = 0

def go_fishing(col) :
    global result
    for i in range(R) : 
        if board[i][col] != 0 and board[i][col] not in dead_shark: 
            size = board[i][col] 
            board[i][col] = 0
            result += size
            dead_shark.add(size)
            return 

def is_inrange(x, y) : 
    return 0<=x<R and 0<=y<C

def move_shark() : 
    new_board = [[0 for _ in range(C)] for _ in range(R)]

    new_shark_info = []
    for r, c, z, s, d in shark_info : 
        if z in dead_shark : continue
        cnt = 0
        cd = d
        nr, nc = r, c
        while cnt != s : 
            nr, nc = nr + dx[cd], nc + dy[cd]
            if not is_inrange(nr, nc) : # 방향 바꾸기
                nr, nc = nr - dx[cd], nc - dy[cd]
                if cd == 0 : cd = 1
                elif cd == 1 : cd = 0
                elif cd == 2 : cd = 3
                else : cd = 2
                nr, nc = nr + dx[cd], nc + dy[cd]
            cnt += 1
        
        new_shark_info.append((nr, nc, z, s, cd))
    
    dead = set()
    dup = set() # 이미 한번 나왔던 좌표 제거용
    new_shark_info = sorted(new_shark_info, reverse=True)
    
    for r, c, z, _, _ in new_shark_info: 
        if (r, c) not in dup : 
            dup.add((r, c))
            new_board[r][c] = z
        else : dead.add(z)

    return new_board, new_shark_info, dead

for pos in range(C) : 
    go_fishing(pos)
    board, shark_info, dead_shark = move_shark()
    
print(result)