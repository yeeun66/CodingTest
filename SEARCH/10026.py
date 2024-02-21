# 적록색약
# 적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력

# 1. 그래프를 우선 입력 받은 상태로 r,g,b 서로 다르다치고 bfs 수행후 구역 갯수 출력 -> 이건 별 문제없음
# 2. 이후, 그래프 변형 -> 이중 반복문 돌면서 G를 모두 찾아 R로 바꾼 후, bfs 수행 후 출력 
import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs() :
    count = 0
    visit = [[0] * N for _ in range(N)]
    queue = deque()
    for i in range(N): 
        for j in range(N): 
            if i == 0 and j == 0 : 
                queue.append((i, j))
                visit[i][j] = True
                count += 1
            else :
                if not visit[i][j] :
                    queue.append((i, j))
                    visit[i][j] = True
                    count += 1
            while queue :
                x, y = queue.popleft()
                for m in range(4) :
                    nx = x + dx[m]
                    ny = y + dy[m]
                    if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == graph[x][y] and not visit[nx][ny]: 
                        queue.append((nx, ny))
                        visit[nx][ny] = True
    return count

N = int(input())

graph = []
for _ in range(N) :
    graph.append(list(map(str, input().rstrip())))

a = bfs()

for i in range(N): 
    for j in range(N): 
        if graph[i][j] == 'G' :
            graph[i][j] = 'R'

b = bfs()
print(a, b)