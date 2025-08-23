# 꼬리잡기놀이
'''
로직
생각해보면, 머리 사람 말고는 앞사람의 자리로 가면 됨, 즉 머리 사람만 앞으로 옮겨주는거임
1. 각 팀별 사람의 좌표 구해놓기
    - 팀 정보 관리 : team (모든 사람의 좌표) <- 근데 이제 맨앞은 머리사람, 맨뒤는 꼬리사람
        - 입력 배열에서 1을 만나면, team의 head좌표로 저장
            상하좌우 탐색하며 2를 만나면 그 방향대로 탐색 (그리고 그 방향의 반대방향이 이 팀의 현재 방향이 됨)
            탐색중 격자 밖(또는 0)을 넘어가면 2또는 3을 찾을 때까지 방향 바꿔가며 탐색
            3을 만나면 좌표 저장후 탐색 종료  
    - 이건 bfs 돌려도 되겠는데? 

k번 라운드 동안 아래를 반복
2. 각 팀은 머리 사람을 따라 한칸 이동
    - 머리사람만 자신의 방향으로 한칸 이동 후 맨앞에 집어넣기 
    - 나머지는 그대로 두고 맨뒤는 제거 (슬라이싱)
3. k라운드에 따른 공이 던져짐 
    - round = k % (4*n)에 따라 공 던져짐
    - round <= n 일때 / round <= 2*n 일 때 / round <= 3*n 일 때 / round <= 4*n 일 때 나눠서 조작
4. 공이 던져졌을 때, 사람을 만나면 점수제공 후 방향 바꾸기
    - 최초의 사람에게 점수 제공 (k번째 사람일 때 k^2만큼)
        - 그 사람이 몇번째 사람인지는 각 팀 탐색하며 알아내야 함
    - 해당 팀은 머리사람과 꼬리사람이 바뀜 (즉 방향이 바뀜)
        - 배열 뒤집기 + 방향 반대로
'''

from collections import deque

dx = [-1, 0, 1, 0] # 상우하좌
dy = [0, 1, 0, -1]

n, m, k = map(int, input().split())
board = []
for _ in range(n) : board.append(list(map(int, input().split())))

team = [[] for _ in range(m)] 
team_dir = [-1 for _ in range(m)] # 각 팀의 현재 방향

def is_inrange(x, y) : 
    return 0<=x<n and 0<=y<n

def bfs(num, x, y) : 
    visited = [[0 for _ in range(n)] for _ in range(n)]
    sx, sy = x, y # 머리사람 
    visited[x][y] = 1
    que = deque()
    que.append((x, y))

    while que : 
        x, y = que.popleft()
        team[num].append((x, y))
        if board[x][y] == 3 : break
        for i in range(4) : 
            nx, ny = x + dx[i], y + dy[i]
            if is_inrange(nx, ny) and not visited[nx][ny] and board[nx][ny] == 2 :
                que.append((nx, ny))
                visited[nx][ny] = 1
                if (x, y) == (sx, sy) : team_dir[num] = (i+2) % 4
                break

            if team_dir[num] == -1 : continue
            if is_inrange(nx, ny) and not visited[nx][ny] and board[nx][ny] == 3 : 
                que.append((nx, ny))
                visited[nx][ny] = 1
                break

cnt = 0
for i in range(n) : 
    if cnt == m : break
    for j in range(n) : 
        if board[i][j] == 1 : 
            bfs(cnt, i, j)
            cnt += 1
        if cnt == m : break

def move_people() : 
    for num in range(m) : 
        sx, sy = team[num][0]
        d = team_dir[num]
        nx, ny = sx + dx[d], sy + dy[d]
        while not is_inrange(nx, ny) or board[nx][ny] == 0 or board[nx][ny] == 2 : 
            d = (d+1) %4
            nx, ny = sx + dx[d], sy + dy[d]
        team_dir[num] = d 
        fx, fy = team[num][-1] # 이전 꼬리사람
        px, py = team[num][-2] # 현재 꼬리사람
        team[num] = [(nx, ny)] + team[num][:-1]

        board[fx][fy] = 4
        board[px][py] = 3
        board[sx][sy] = 2 # 현재 두번째 사람 (이전 머리)
        board[nx][ny] = 1 # 현재 머리사람 

def find_order(x, y) : 
    for i in range(m) : 
        for j in range(len(team[i])) : 
            if team[i][j] == (x, y) : 
                return i, j+1

def throw_ball(rounds) :
    global result
    num, order = -1, -1
    if 1 <= rounds <= n : 
        i = rounds-1 # 행 고정
        for j in range(n) : 
            if 0 < board[i][j] < 4 : 
                num, order = find_order(i, j)
                break

    elif n < rounds <= 2*n : 
        rounds %= n
        if rounds == 0 : j = n-1
        else : j = rounds-1 # 열 고정 
        for i in range(n-1, -1, -1) : 
            if 0 < board[i][j] < 4 : 
                num, order = find_order(i, j)
                break

    elif 2*n < rounds <= 3*n : 
        rounds %= n
        if rounds == 0 : i = 0
        else : i = n-rounds # 행 고정
        for j in range(n-1, -1, -1) : 
            if 0 < board[i][j] < 4 : 
                num, order = find_order(i, j)
                break
    else : 
        rounds %= n
        if rounds == 0 : j = 0
        else : j = n-rounds # 열 고정 
        for i in range(n) : 
            if 0 < board[i][j] < 4 : 
                num, order = find_order(i, j)
                break
    
    if (num, order) != (-1, -1) : 
        result += (order**2)
        team[num] = team[num][::-1]
        sx, sy = team[num][0]
        fx, fy = team[num][-1]
        board[sx][sy] = 1
        board[fx][fy] = 3
        team_dir[num] = (team_dir[num] + 2) % 4


result = 0
for turn in range(1, k+1) :
    move_people()
    throw_ball(turn%(4*n))

print(result)