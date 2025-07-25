# 연구소 3
# 연구소의 상태가 주어졌을 때, 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간 구하기 

'''
로직
0 빈칸 1 벽 2 비활성 바이러스
1. 바이러스 전체 중 M개를 뽑는 모든 경우의 수로 아래 수행 - 조합 함수 쓰기
2. 선택된 바이러스는 활성 상태로 변경 - M개의 좌표를 모두 큐에 넣고 bfs 수행
3. bfs 수행
    - 큐에서 하나씩 꺼내며 상화좌우 탐색 (경계 내에서 벽이 아니면)
    - 방문 기록은 처음 활성 바이러스는 1로, 그 뒤로는 부모+1로 기록
4.  - 큐 엠티이면, 바이러스가 모두 퍼졌는지 검사
        - 벽이 아닌데 방문기록이 0인 칸이 있다면, 모두 안퍼진 것
        - 그럼 그냥 리턴
    - 바이러스가 모두 퍼졌다면 최소 시간 업데이트 min(min_val, final_visit-1)

5. 모든 수행 끝난 후 min_val이 N ** 3 이면 -1 출력
- 아니면 min_val 출력
'''

from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
board = []
for _ in range(N) : board.append(list(map(int, input().split())))

virus = []
for i in range(N) :
    for j in range(N) :
        if board[i][j] == 2 : virus.append((i, j))

def is_inrange(x, y) : 
    return 0<=x<N and 0<=y<N

def bfs(lst) :
    final_visit = 1
    visited = [[0 for _ in range(N)] for _ in range(N)]
    que = deque()
    for x, y in lst : 
        que.append((x, y))
        visited[x][y] = 1

    while que : 
        x, y = que.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if is_inrange(nx, ny) and board[nx][ny] != 1 and not visited[nx][ny]: 
                visited[nx][ny] = visited[x][y] + 1
                que.append((nx, ny))
                if board[nx][ny] == 0 : final_visit = visited[nx][ny]
                
        
    for i in range(N) :
        for j in range(N) :
            if board[i][j] == 0 and visited[i][j] == 0 : 
                return N ** 3
    
    return final_visit-1

min_sec = N ** 3
for cb in combinations(virus, M) : 
    min_sec = min(min_sec, bfs(cb))

if min_sec == N ** 3 : print(-1)
else : print(min_sec)
