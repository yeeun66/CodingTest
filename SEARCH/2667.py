# 단지번호붙이기
#  지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램
# BFS 사용 
# DFS도 가능 -> 다음에 해보기 
from collections import deque

def bfs(graph, x, y) :
    # 상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0  #탐색중인 위치 0으로 바꿔 다시 방문하지 않도록 함
    cnt = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4): # 상하좌우 움직이기
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny <0 or ny >= N: # 경계 넘어간 경우
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0 # 다시 방문 안하도록
                queue.append((nx,ny))
                cnt += 1
    return cnt

N = int(input())

# 행렬 만들기
graph = [list(map(int, input())) for _ in range(N)] # N은 행의 개수 

count = [bfs(graph, i, j) for i in range(N) for j in range(N) if graph[i][j] == 1]
count.sort()

print(len(count))
for i in range(len(count)):
    print(count[i])