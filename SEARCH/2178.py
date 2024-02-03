# 미로 탐색
# BFS

from collections import deque

N, M = map(int, input().split())

def bfs(graph) :
    # 우하좌상
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    cnt = 0
    queue = deque()
    queue.append((0,0))
    graph[0][0] = 0
    cnt = 1

    while queue :
        # flag = 0
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M : continue
            
            if graph[nx][ny] == 1 :
                graph[nx][ny] = 0
                queue.append((nx,ny))
                cnt += 1
                # flag = 1
                # px = x
                # py = y
                break

        # if flag == 0 : 
        #     graph[nx][ny] = 0
        #     queue.append((px,py))
        #     cnt -= 1

    return cnt

graph = [list(map(int, input())) for _ in range(N)]
count = bfs(graph)
print(count)