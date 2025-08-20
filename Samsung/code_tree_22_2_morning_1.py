# 싸움땅 
'''
로직 
0. 사용할 배열 정리
    - board: 총이 있는 보드, 나중에 여러개가 될 때는 [1, 3, 3] 이런식으로 확장 가능하게 모두 3차원 배열로 만들어 두기
    아래 배열들은 0번 플레이어 자리 비워두기
    - player_pos : 플레이어 위치. x, y = 현재 위치 좌표
    - player_dir : 플레이어의 현재 방향 d -> 방향은 0~3 : 상우하좌
    - player_power : s, p = 플레이어의 초기 능력치, 현재 가지고 있는 총의 공격력.
    - points : 각 플레이어가 획득한 포인트

k라운드 동안 다음을 반복
1~m번 플레이어 순서대로 아래 로직을 모두 한번씩 수행
1. 본인 방향으로 한칸 이동 (격자를 벗어나는 경우 정반대로 방향 바꿔서 이동) - move_player()
2. 
    (1) 이동한 곳에 다른 플레이어 없다면, 해당 칸에 총이 있는지 확인. 
        - 총이 있다면 획득. 이미 있다면, 더 좋은걸로 획득하고 소지한거 내려놓기 - gain_gun()
    (2) 이동한 곳에 다른 플레이어 있다면, 싸우기 - fight()
        - (초기능력치+총의공격력) 을 비교 
            - 수치가 같은 경우, 초기 능력치가 더 큰 플레이어 승리
        - 승리 플레이어: 아까 비교한 값의 차이만큼 능력치 획득
        - 패배 플레이어: 가지고 있는 총 격자에 내려놓고 방향대로 한칸 이동
            - 이때 이동할 칸이 격자 밖이거나, 누가 있으면, 오른쪽으로 90도씩 움직이면서 갈 곳 찾아 이동
            - 이동한 칸에 총이 있으면, 가장 좋은 총 획득하고 나머지 내려놓기 - gain_gun()
        - 승리 플레이어: 현재 칸의 가장 좋은 총 획득 후 나머지 내려놓기 - gain_gun()
'''

import sys; input = sys.stdin.readline

dx = [-1, 0, 1, 0] # 상우하좌
dy = [0, 1, 0, -1]

n, m, k = map(int, input().split())
board = []
for _ in range(n) : 
    tmp = list(map(int, input().split()))
    temp = []
    for t in tmp : temp.append([t])
    board.append(temp)

points = [0 for _ in range(m+1)]
player_pos = [(-1, -1, -1)]
player_dir = [-1]
player_power = [(-1, -1)]
for _ in range(m) : 
    x, y, d, s = map(int, input().split())
    player_pos.append((x-1, y-1))
    player_dir.append(d)
    player_power.append((s, 0))

def is_inrange(x, y) : 
    return 0<=x<n and 0<=y<n 

def move_player(num) : 
    x, y = player_pos[num]
    d = player_dir[num]

    nx, ny = x + dx[d], y + dy[d]
    if not is_inrange(nx, ny) : 
        d = (d + 2) % 4 # 방향 바꿔 
        nx, ny = x + dx[d], y + dy[d]
    
    player_pos[num] = (nx, ny)
    player_dir[num] = d 

def gain_gun(x, y, num) : 
    board[x][y].sort()
    s, p = player_power[num]
    max_v = board[x][y][-1]
    if player_power[num][1] == 0 : 
        player_power[num] = (s, max_v)
        board[x][y][-1] = 0
        return
    
    if max_v > player_power[num][1] : 
        board[x][y][-1] = player_power[num][1]
        player_power[num] = (s, max_v)

    return

def fight(x, y, num1, num2) :
    
    power1 = sum(player_power[num1])
    power2 = sum(player_power[num2])
    winner, loser = 0, 0

    if power1 > power2 : 
        winner, loser = num1, num2
    elif power1 < power2 : 
        winner, loser = num2, num1
    else : 
        p1 = player_power[num1][0]
        p2 = player_power[num2][0]
        if p1 > p2 : 
            winner, loser = num1, num2
        else :
            winner, loser = num2, num1
    
    points[winner] += abs(power1-power2) # 위너 점수 획득

    if player_power[loser][1] != 0 : 
        if board[x][y] == [0] : board[x][y] = [player_power[loser][1]] # 루저 총 내려놓기 
        else : board[x][y].append(player_power[loser][1]) 
    s, p = player_power[loser]
    player_power[loser] = (s, 0)

    d = player_dir[loser]
    nx, ny = x + dx[d], y + dy[d]
    while not is_inrange(nx, ny) or (nx, ny) in player_pos: 
        d = (d + 1) % 4
        nx, ny = x + dx[d], y + dy[d]
    
    player_pos[loser] = (nx, ny)
    player_dir[loser] = d # 이거 방향 업데이트 꼭 해줘야함! 문제에 언급 없어서 그냥 두 경우 다 해봄
    if board[nx][ny] != [0] : gain_gun(nx, ny, loser)

    player_pos[winner] = (x, y)
    if board[x][y] != [0] : gain_gun(x, y, winner)


for turn in range(1, k+1) : 

    for i in range(1, m+1) :  
        move_player(i) # 1
        x, y = player_pos[i]
        player_pos[i] = (-1, -1)
        if (x, y) not in player_pos : # 2-1
            player_pos[i] = (x, y)
            if board[x][y] != [0] : gain_gun(x, y, i) 
        else : # 2-2
            for j in range(1, m+1) :
                if i != j and player_pos[j] == (x, y) : 
                    fight(x, y, i, j) 
                    break

## 정답
for i in range(1, m+1) : print(points[i], end=" ")
