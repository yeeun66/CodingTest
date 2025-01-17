# 헌내기는 친구가 필요해

# 도연이가 다니는 대학의 캠퍼스는 N x M 크기이며 캠퍼스에서 이동하는 방법은 벽이 아닌 상하좌우로 이동하는 것이다. 
# 캠퍼스에서 도연이가 만날 수 있는 사람의 수를 출력하는 프로그램을 작성해보자.

# 입력
# 첫째 줄에는 캠퍼스의 크기를 나타내는 두 정수 N, M(1이상 600이하)이 주어진다.
# 둘째 줄부터 N개의 줄에는 캠퍼스의 정보들이 주어진다. O는 빈 공간, X는 벽, I는 도연이, P는 사람이다. I가 한 번만 주어짐이 보장된다.
# 출력
# 첫째 줄에 도연이가 만날 수 있는 사람의 수를 출력한다. 단, 아무도 만나지 못한 경우 TT를 출력한다.

# 방법:
# 도연이(I) 위치부터 bfs 탐색 시작, 
    # 상하좌우로 탐색시 O(빈공간)이면 계속 탐색, P(사람)이면 count 증가 후 계속 탐색 (탐색한 위치는 X로 변경하기)
    # X이면 무시
# 최종 카운트가 0이 아니면 출력 (0이면 TT 출력)

import sys
from collections import deque

input = sys.stdin.readline
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y) :
    cnt = 0
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 'X'

    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != 'X' :
                if graph[nx][ny] == 'P' : cnt += 1
                queue.append((nx, ny))
                graph[nx][ny] = 'X'
    return cnt


N, M = map(int, input().split())
graph = [[] for _ in range(N)] # 행 만큼만 만들어도 됨

for i in range(N) :
    graph[i].extend(input().rstrip()) # 줄바꿈 제외하고 원소별로 하나씩 extend 해주기

count = 0
for i in range(N) :
    for j in range(M) :
        if graph[i][j] == 'I' : 
            count = bfs(i, j) 
            break

if count == 0 : print("TT")
else : print(count)