# 나이트의 이동

# 상하좌우 이동의 확장판 (그림의 맨왼쪽 위부터 1번~8번 이동이라 하자) - 문제 조건 상 BFS 임
# 1. 그래프 초기화 (체스판길이 lxl 만큼 모두 0으로 초기화)
    # 처음 입력 받은 시작 지점은 0로 표시
    # 도착 지점은 -100으로 표시
# 2. BFS 탐색
    # 8번 탐색하면서 방문하지 않은 곳이면(값이 0이면), 방문 표시하고(부모 노드 값 + 1)
    # 큐에 추가한다. 
    # 값이 -100인걸 만나면(도착하면), 자신의 루트 노드의 값에 1 더한 값을 리턴

import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, -2, -2, -1, 1, 2, 1, 2] # x가 세로 (행)
dy = [-2, -1, 1, 2, -2, -1, 2, 1] # y가 가로 (열)

def bfs(x, y) :
    queue = deque()
    queue.append((x, y))
    # graph[x][y] = 1
    while queue :
        x, y = queue.popleft()
        for i in range(8) : 
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l:
                if graph[nx][ny] == -100 : # 도착하면
                    return (graph[x][y] + 1)
                elif graph[nx][ny] == 0 :
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))


T = int(input())
for _ in range(T) :
    count = 0
    l = int(input()) # 체스판 길이 
    a, b = map(int, input().split())
    endx, endy = map(int, input().split())
    graph = [[0] * l for _ in range(l)]
    graph[a][b] = 0
    graph[endx][endy] = -100
    # print(graph)
    if a == endx and b == endy : print(count)
    else: print(bfs(a, b))