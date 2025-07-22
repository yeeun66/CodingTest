# 알고스팟
# 현재 (1, 1)에 있는 알고스팟 운영진이 (N, M)으로 이동하려면 벽을 최소 몇 개 부수어야 하는지 구하기
# 다익스트라 개념 써야 함
    # BFS로 모든 경우 다 탐색하면 시간초과 or 메모리 초과

'''
다익스트라 로직
상태 관리 : heapq에 (비용, 좌표)를 넣어 관리 / 최단 거리(최소 비용)은 dist라는 2차원 배열에 따로 넣어 관리
- 해당 도착 칸에 대해 최소 비용으로 업데이트를 해주는 과정.
- 다익스트라 수행이 끝나면 dist 배열의 각 최소비용이 저장되게 됨.

1. 큐에 처음에 (0, 0, 0)을 넣고 시작
2. 하나씩 pop하면서 
    - 현재 비용이 최단거리 보다 크다면 컨디뉴 - 이미 더 적은 비용으로 방문한 적이 있는 노드라면 무시
    - 인접 칸 탐색하며 범위 내에 있고, 아직 방문 안했다면 (배열값+cost < dist)
        dist 업데이트 하고, 큐에 (비용, 좌표) 추가 

* 여기서 중요한 것: 벽(=1)이 cost라고 생각하면 편함. cost 1: 벽 부순 갯수 1개 *
3. 그럼 최종 완성된 dist[N-1][M-1] 이 최소비용(벽 부순 갯수 가장 작은) 결과가 됨
'''

import heapq
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

M, N = map(int, input().split())
board = []
for _ in range(N) : board.append(list(map(int, input().strip())))

def is_inrange(x, y) :
    return 0<=x<N and 0<=y<M

inf = N*M + 1
dist = [[inf for _ in range(M)] for _ in range(N)] # 최단거리 리스트 
q = [] # heapq로 사용할 배열 

heapq.heappush(q, (0, 0, 0)) # cost, x좌표, y좌표
dist[0][0] = 0 
while q : 
    cost, x, y = heapq.heappop(q)

    if cost > dist[x][y] : continue # 이미 더 적은 비용으로 방문한 적이 있는 노드라면 무시

    for i in range(4) :
        nx, ny = x + dx[i], y +dy[i]
        if is_inrange(nx, ny) and cost + board[nx][ny] < dist[nx][ny] :
            dist[nx][ny] = cost + board[nx][ny] # 최소비용으로 업데이트 
            heapq.heappush(q, (dist[nx][ny], nx, ny))

print(dist[N-1][M-1])