# 연구소
# 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.
# 연구소는 크기가 N×M인 직사각형이다. 또한 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다
# 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 
# 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
# 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다. 
# 벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다. 지도가 주어졌을 때 가능한 안전 영역 크기의 최댓값 구하기
# 세로 크기 N과 가로 크기 M (3 ≤ N, M ≤ 8)

# 방법:
# 벽을 세우는 경우의 수 모두 계산한 후, 안전 영역 구하고 최대 안전 영역 출력 => 이거를 다 해도 시간 복잡도 괜찮다고 함. 이유는 나도 모름
# 예를들어 4*6 matrix 에서 빈칸이 17개라면, 그 중 3개를 골라 1로 만들어야 하므로 17C3 만큼 반복해야 함
    # from itertools import combinations <- 이거 사용!

# 1. 배열 입력 받기
# 2. combinations 사용하여 (0개수)C(3) 만큼 아래를 반복 <= 이때 원래 값이 0인 요소들의 위치를 모두 튜플로 저장해둬야 함
    # 2-1. 원본 배열을 copy 한다 (무조건 copy()로 해야함) 
    # 2-2. 등장한 조합의 좌표의 값을 1로 바꾼다.
    # 2-3. 바꾼 배열을 가지고 bfs를 진행한다. (사실 이건 dfs해도 돼)
        # bfs는 2를 찾아서 그 좌표로 bfs 시작 (이것도 원본 배열에서 새로운 배열에 바이러스들 좌표 만들어놓기)
        # 0이면 그 위치를 2로 바꾸고 큐에 넣고 해서 반복
    # 2-4. bfs가 끝나면 해당 배열에서 0의 갯수를 세고 그 갯수를 이전의 갯수와 비교하여 최대로 업데이트

import sys
import copy
from itertools import combinations
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y) :
    queue = deque()
    queue.append((x, y))

    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and new[nx][ny] == 0 :
                new[nx][ny] = 2
                queue.append((nx, ny))


N, M = map(int, input().split())
origin = []
for _ in range(N) : origin.append(list(map(int, input().split())))

zero = []
virus = []
[zero.append((i, j)) for i in range(N) for j in range(M) if origin[i][j] == 0]
[virus.append((i, j)) for i in range(N) for j in range(M) if origin[i][j] == 2]

max_safety = 0
f1, f2 = 1, 1
for comb in combinations(zero, 3) :
    new = copy.deepcopy(origin)
    for i in range(3) :
        a = comb[i][0]
        b = comb[i][1]
        new[a][b] = 1

    for i in range(len(virus)) : # 바이러스 수 만큼 bfs 수행
        a = virus[i][0]
        b = virus[i][1]
        bfs(a, b)
        
    cnt = 0 # 2차원 배열에서 0 갯수 셀 때 냅다 count하면 안됨
    for i in range(N) :cnt += new[i].count(0)

    max_safety = max(max_safety, cnt)
    
print(max_safety)