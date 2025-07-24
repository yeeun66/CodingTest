# 다리 만들기
'''
로직 
1. 붙어있는 덩어리(=대륙)을 찾아서 대륙 별로 번호를 매긴다 - bfs
2. 모든 대륙에 대하여 1번 부터 ~ 가장 짧은 다리 길이 탐색 시작
    - 예를 들어, 1번 땅 끝에서 시작하여 바다를 거쳐 다른 대륙에 도착하기 까지 바다의 칸수 구한다
    - 도착했을 때 거리가 현재 가장 짧은 거리라면 그 다리로 업데이트 한다
    - 이때 시작하는 땅 위치는 4면이 모두 같은 육지로 둘러쌓여 있다면 다른 대륙 탐색X
    - 각 대륙 마다, 다른 대륙에 도착하는 최소 거리를 현재 최소와 비교하여 리턴 
    - ** 중요한건 이동할 곳이 0일 때 이전 도착 거리 보다 지금 도착 거리가 더 짧으면 업데이트 해줘야 함
3. 그러면 최종 최소 거리 출력 

'''

from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
board = []
for _ in range(N) : board.append(list(map(int, input().split())))

min_dist = N ** 2
visited = [[0 for _ in range(N)] for _ in range(N)]

def is_inrange(x, y) : 
    return 0<=x<N and 0<= y<N

def bfs(x, y, n, visited) : 

    que = deque()
    que.append((x, y))
    while que :
        x, y = que.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if is_inrange(nx, ny) and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = 1
                board[nx][ny] = n
                que.append((nx, ny))

    return board, visited

def find_bridge(x, y, num) :
    cur_min = N ** 2
    visited = [[0 for _ in range(N)] for _ in range(N)]
    dist = [[0 for _ in range(N)] for _ in range(N)] # 0을 만나면 카운트 증가 / 자신이 아닌 양수를 만나면 cur_min 업데이트

    que = deque()
    que.append((x, y))

    visited[x][y] = 1
    while que: 
        x, y = que.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if is_inrange(nx, ny) and not visited[nx][ny] :
                if board[nx][ny] == num: 
                    que.append((nx, ny))
                    visited[nx][ny] = 1
                elif board[nx][ny] == 0 : 
                    que.append((nx, ny))
                    visited[nx][ny] = 1
                    dist[nx][ny]  = dist[x][y] + 1
                else : 
                    cur_min = min(cur_min, dist[x][y])
                    
            elif is_inrange(nx, ny) and board[nx][ny] == 0 : # 이동할 곳이 0인 경우 
                dist[nx][ny] = min(dist[nx][ny], dist[x][y] + 1) # 최단 경로로 업데이트

    return cur_min

# 대륙 별 번호 부여
num = 1
for i in range(N) :
    for j in range(N) :
        if board[i][j] == 1 and not visited[i][j]: 
            visited[i][j] = 1
            board[i][j] = num
            board, visited = bfs(i, j, num, visited)
            num += 1

# 각 대륙별 탐색
k = 1
for i in range(N) :
    if k > num : break
    for j in range(N) :
        if k > num : break
        if board[i][j] == k : 
            min_dist = min(min_dist, find_bridge(i, j, k))
            k+= 1
            
print(min_dist)