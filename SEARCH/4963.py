# 섬의 개수
# 정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램
# 각 테스트 케이스에 대해서, 섬의 개수를 출력
# 한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 
# 두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 
# 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다.
# 둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.
# 입력의 마지막 줄에는 0이 두 개 주어진다.

# 0 0 입력 받을 때 까지 테스트 케이스 입력받기 반복
# h 만큼 지도 입력 받기
# 다른 문제와 다른 점: 대각선도 고려

import sys
from collections import deque

input = sys.stdin.readline

# 상하좌우대각선
dx = [-1, 1, 0, 0, -1, 1, 1, -1] 
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(x, y) :
    queue = deque()
    queue.append([x, y])
    graph[x][y] = 0
    while queue :
        x, y = queue.popleft()
        for m in range(8) :
            nx = x + dx[m]                            
            ny = y + dy[m]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1 :
                queue.append([nx, ny])
                graph[nx][ny] = 0 # 시간 초과 문제는 여기였다!! -> 큐에 넣은 것도 바로바로 방문 상태 업데이트 해줘야 중복 삽입 막을 수 있다!!
            
while True :
    w, h = map(int, input().split())
    if w == 0 and h == 0 : break
    graph = []
    [graph.append(list(map(int, input().split()))) for _ in range(h)]
    count = 0
    for i in range(h) :
        for j in range(w) :
            if graph[i][j] == 1 : 
                bfs(i, j)
                count += 1
    print(count)