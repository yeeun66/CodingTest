# 코드트리 빵 
'''
로직
우선순위 상좌우하 
최단거리 - 현재 최단거리가 아니고 도달하기 까지의 최단거리를 말함

** 배열 및 상태 관리
    - goal 배열: 편의점에 도착한 사람의 번호 저장
    - board 배열: 게임판. 1은 이동가능한 베이스 캠프. 0은 빈칸. -1은 이동 불가능한 칸
    - store 배열: 각 참가자가 가야하는 편의점 좌표 
        - store[0]은 0번 참가자가 가야하는 편의점 좌표
    - people 배열: 각 사람들의 현재 좌표. 
        - 초기는 (-1, -1). 베이스 캠 정해지면 그 좌표로 갱신 

m명 모두 편의점에 도착할 때 까지 아래를 반복 
1. 격자 내에 있는 사람들 모두 원하는 편의점을 향해 최단거리로 한칸 이동 - move_people 
    - n < t 이고 아직 안도착한 사람일 때, (goal에 있지 않은 사람) 한 칸 이동
    - 상좌우하 한칸 중 이동가능한 칸을 모두 (좌표, 방향) 형태로 큐에 넣고 편의점 만날 때 까지 bfs 돌림
    - 이때 편의점 도착한 거리가 가장 짧은 방향으로 칸으로 한칸 이동

2. 편의점에 도착했다면, 해당 편의점에서 이동 멈춤. 
    - 이제 해당 편의점은 다른 사람들이 못지나가게 됨 -> 보드에 -1로 표시
    - 도착한 사람 표시
    - 이건 3번 시작 전에 보드 업데이트!

3. 현재 시간이 t분일 때, t<=m 을 만족할 때, 
    - t번 사람은 자신이 가고 싶은 편의점과 가장 가까운 베이스 캠프에 들어감
        - 원하는 편의점에서 남아있는 베이스 캠프(1인칸) 탐색 - find_base_camp
        - 탐색된 최소 칸이 여러개이면 행작, 열작 순으로 들어감 - sort
    - 이때부터 다른 사람들은 해당 베이스 캠프가 있는 칸을 못지나감 -> 보드에 -1로 표시
        - 자신의 베이스캠도 나중에 못지나감 

4. 종료 조건 
    - 편의점 도착한 사람이 m명이면, 즉 모두 도착하면, 현재 초(t) 출력 후 종료
'''
'''
디버깅
(1) TC 5번에서 틀린 이유: 
    1, 2번 수행 후 3번(베이스 캠프 가기) 수행 전에 보드 한번 업데이트 해줘야 하는데, 안하고 마지막에 업데이트 해서 틀렸던 것!
    문장이 애매하게 나와있긴 했지만 충분히 알 수 있는 문장 "격자에 있는 모든 사람들이 이동한 뒤에 해당 칸을 지나갈 수 없어짐에 유의합니다"
    => 처음에 모든 턴이 끝난 이후 못 지나가는 줄 알았지만, 그게 아니라 모든 사람 이동 (즉 베이스 캠프로 가는 사람 제외) 후에 못 지나가는 거였음
(2) TC 99번에서 틀린 이유: 
    자신의 베이스캠프로도 다시 돌아가면 안되는데, 나중에 돌아가는 경우 발생했음

'''
from collections import deque
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

n, m = map(int, input().split())
board = []
for _ in range(n) : board.append(list(map(int, input().split())))
store = []
people = []
base_camp = []
for _ in range(m) : 
    x, y = map(int, input().split())
    store.append((x-1, y-1))
    people.append((-1, -1))
    base_camp.append((-1, -1))

def is_inrange(x, y) : 
    return 0<=x<n and 0<=y<n

def bfs(num) :
    visited = [[0 for _ in range(n)] for _ in range(n)]
    ex, ey = store[num] # num이 원하는 편의점
    sx, sy = people[num] # num의 현재 좌표 
    visited[sx][sy] = 1
    que = deque()
    for i in range(4) : 
        nx, ny = sx + dx[i], sy + dy[i]
        if is_inrange(nx, ny) and board[nx][ny] != -1 : 
            if (nx, ny) == (ex, ey) : return i # 그냥 이 방향으로 한칸만 움직이면 바로 도착 
            else : 
                que.append((nx, ny, i)) # 좌표와 방향 
                visited[nx][ny] = 1
    
    while que : 
        x, y, d = que.popleft() 
        for i in range(4) : 
            nx, ny = x + dx[i], y + dy[i]
            if is_inrange(nx, ny) and not visited[nx][ny] and board[nx][ny] != -1 : 
                if (nx, ny) == (ex, ey) : return d
                else : 
                    que.append((nx, ny, d)) # 좌표와 부모의 방향  
                    visited[nx][ny] = 1


goal = set()
def move_people(t) : 
    new_board = [b[:] for b in board]
    for i in range(m) : 
        if i+1 >= t : break
        if i in goal : continue
        direct = bfs(i)
       
        x, y = people[i]
       
        nx, ny = x + dx[direct], y + dy[direct]
        people[i] = (nx, ny)
        sx, sy = store[i]
        if (sx, sy) == (nx, ny) : # 편의점 도착
            new_board[sx][sy] = -1
            goal.add(i)
    
    return new_board

def find_base_camp(t) : 
    
    new_board = [b[:] for b in board]
    sx, sy = store[t-1] # t번 사람이 원하는 편의점
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[sx][sy] = 1

    que = deque()
    que.append((sx, sy))
    min_dist = n ** 3
    candidate = []
    while que : 
        x, y = que.popleft()
        if visited[x][y] >= min_dist : break
        for i in range(4) : 
            nx, ny = x + dx[i], y + dy[i]
            if is_inrange(nx, ny) and not visited[nx][ny] and board[nx][ny] != -1 :
                if board[nx][ny] == 1 and min_dist >= visited[x][y] + 1: 
                    min_dist = visited[x][y] + 1
                    candidate.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                else : 
                    que.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    
    candidate.sort()

    fx, fy = candidate[0]
    new_board[fx][fy] = -1
    people[t-1] = (fx, fy)
    base_camp[t-1] = (fx, fy)
    return new_board
    

time = 0
while True : 
    time += 1
    first_new_board = move_people(time) # 1, 2
    # 이때 편의점 도착한 사람들 정보 반영해 줘야 함!!
    for i in range(n) : 
        for j in range(n) : 
            if first_new_board[i][j] == -1 : board[i][j] = -1 

    if time <= m : 
        board = find_base_camp(time) # 3
    
    if len(goal) == m : 
        print(time)
        exit()
