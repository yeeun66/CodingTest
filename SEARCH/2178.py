# 미로 탐색
# BFS

#이것만 제대로 하면 BFS 거의 가능
# 알고리즘 간단 정리
# 1. 미로 입력: 이차원 리스트 그래프로 입력 받기
# 2. 상하좌우로 탐색할 리스트 선언
# 3. bfs() 함수 구현
# 3-1. 좌표를 큐에 넣어
# 3-2. 프론트 좌표 뽑아서 이 좌표로 상하좌우 움직인 후, 
#      값이 1이면 큐에 넣고 그 위치에 이전값 + 1 을 하면 얼만큼 지나왔는지 알 수 있음
# 3-3. 도착 위치의 배열 값 출력 (= 최종 얼마나 지나왔는지 값 나옴)
import sys
from collections import deque

def bfs():
    
    queue = deque()
    queue.append((0,0))

    while queue:
        x, y = queue.popleft()

        for i in range(4): # 상하좌우
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1: # 미로 범위 안벗어나고, 위치에 1이 있으면 큐에 넣어
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1 # 방금 큐에 추가한 값에 이전 값 + 1을 넣어 (지나간 갯수 count)
    
    return graph[n-1][m-1] # 도착값 리턴

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

# 상하좌우
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

print(bfs())