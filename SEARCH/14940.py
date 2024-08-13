# 쉬운 최단거리
# 지도가 주어지면 모든 지점에 대해서 목표지점까지의 거리를 구하여라.
# 문제를 쉽게 만들기 위해 오직 가로와 세로로만 움직일 수 있다고 하자.

# n*m 개의 입력이 주어지면 
# 0은 갈 수 없는 땅이고 1은 갈 수 있는 땅, 2는 목표지점이다. 입력에서 2는 단 한개이다.

# 각 지점에서 목표지점까지의 거리를 출력한다. 원래 갈 수 없는 땅인 위치는 0을 출력하고, 
# 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력한다.

# 값이 2인 배열의 인덱스를 반환해서 그걸 시작 노드로 두고 bfs 수행

from collections import deque
import sys

# 상하좌우
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs(x, y) :
    queue = deque()
    queue.append((x, y))
    visit[x][y] = 1
    graph[x][y] = 0

    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 0 and visit[nx][ny] == -1:
                visit[nx][ny] = 1
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


input = sys.stdin.readline
n, m = map(int, input().split()) # 세로, 가로 (행, 열)

graph = []
for _ in range(n) :
    graph.append(list(map(int, input().split())))

visit = [[-1 for _ in range(m)] for _ in range(n)]
index = 0
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 2 :
            bfs(i, j)
            index = 1
            break
    if index : break

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 1 and visit[i][j] == -1 :
            graph[i][j] = -1

for i in range(n) :
    print(*graph[i])