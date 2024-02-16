# 유기농 배추
# BFS
# 이 문제 뭔가 미로 + 연결 요소

# 상하좌우 탐색. 미로 처럼 그래프 값 증가 시켜(굳이 증가 안시켜도 1만 아닌 값으로 바꾸면 됨).
# 상하좌우 모두 1이 없다? 함수 리턴하고 지렁이 값 증가.
# bfs 함수 들어가기 전 조건은 배열 값이 1인거 -> 이건 어떻게 찾지, 이중반복문 쓰면 됨
import sys
from collections import deque

input = sys.stdin.readline

# 상하좌우
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs(x,y):
    
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        # 상하좌우 움직이면서 탐색
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 1 :
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    return

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split()) # 배추 밭의 가로, 세로, 배추 갯수
    count = 0
    graph = [[0]*N for _ in range(M)]
    for _ in range(K) :
        a, b = map(int, input().split())
        graph[a][b] = 1

    for i in range(M) :
        for j in range(N) :
            if graph[i][j] == 1:
                bfs(i,j)
                count += 1
    print(count)