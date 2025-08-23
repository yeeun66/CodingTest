# 보물섬
# 보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다. 
# 보물 지도가 주어질 때, 보물이 묻혀 있는 두 곳 간의 최단 거리로 이동하는 시간 구하기
'''
로직
1. 모든 육지에 대해 bfs 돌려서 마지막까지의 거리 구한다 (방문 배열 활용)
2. 현재 최대값과 비교 후 업데이트 한다
3. 최종 최댓값 출력
'''

from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
board = []
for _ in range(N) : board.append(list(map(str, input().strip())))

def is_inrange(x, y) : 
    return 0<=x<N and 0 <= y < M

def bfs(x, y) : 
    global result
    visited = [[0 for _ in range(M)] for _ in range(N)]
    que = deque()
    que.append((x, y))
    visited[x][y] = 1

    while que : 
        x, y = que.popleft()
        fin_dist = visited[x][y]
        for i in range(4) : 
            nx, ny = x + dx[i], y + dy[i]
            if is_inrange(nx, ny) and not visited[nx][ny] and board[nx][ny] == 'L' : 
                visited[nx][ny] = visited[x][y] + 1
                que.append((nx, ny))

    result = max(result, fin_dist-1)


result = -1
for i in range(N) : 
    for j in range(M) : 
        if board[i][j] == 'L' : 
            bfs(i, j)

print(result)