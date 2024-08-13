# 영역 구하기
# M, N과 K 그리고 K개의 직사각형의 좌표가 주어질 때, 
# K개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어지는지, 그리고 분리된 각 영역의 넓이가 얼마인지를 구하여 이를 출력하는 프로그램을 작성하시오.

# 첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다. 
# 둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다. 
# 모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다. 입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다.

# 첫째 줄에 분리되어 나누어지는 영역의 개수를 출력한다. 
# 둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력한다.

# ---------- 알고리즘 ---------- 
# 연결 요소 구하는 접근으로 가면 될듯
# 메인에서 bfs를 시작 노드 넣어가면서 돌린다.
    # 방문하지 않은 노드를 시작점으로.
    # 현재 직사각형 영역은 1로 바꾸어 방문 한걸로 친다.
    # bfs 한 번 돌 때 마다 카운트 +1, And 영역 넓이 리턴 (이건 bfs내에서 계산)
    # 근데 이제 bfs에서 좌표를 파라미터를 받아서 좌표 영역 탐색 (상하좌우 배열 사용)

from collections import deque
import sys

# 상하좌우
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs(x, y) :
    region = 0
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 1
    while queue :
        x, y = queue.popleft()
        region += 1
        for i in range(4) : # 상하좌우 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 0 :
                graph[nx][ny] = 1 
                queue.append((nx, ny))
    return region


input = sys.stdin.readline
M, N, K = map(int, input().split())

# 그래프 초기화 
graph =[[0 for _ in range(N)] for _ in range(M)]
for _ in range(K) :
    x1, y1, x2, y2 = map(int, input().split()) # 왼쪽 아래, 오른쪽 위 좌표
    for i in range(y1, y2) :
        for j in range(x1, x2) :
            graph[i][j] = 1

# bfs 돌리기
count = 0 # 분리된 영역 갯수
result = [] # 각 영역의 넓이
for i in range(M) :
    for j in range(N) :
        if graph[i][j] == 0 :
            re = bfs(i, j)
            count += 1 
            result.append(re)

result.sort()
print(count)
print(*result)