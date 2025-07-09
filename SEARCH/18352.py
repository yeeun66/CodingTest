# 특정 거리의 도시 찾기
# 이전에 다익스트라로 풀긴했지만, BFS로 다시 풀어보기
"""
0. 단방향 그래프 구성 -> bfs로 최단 거리 체크
    - (N+1)크기의 2차원 리스트 생성후 입력으로 저장 

1. bfs 탐색
    - 시작 노드부터 각 노드에 방문
    - 방문 하면 바로 방문처리 해야 최단 경로가 됨
    - 이때 방문처리 값으로 길이 구함
    - 길이가 K이면 출력 배열에 저장

2. 출력 배열 오름차순 정렬 후 출력
    - 위 배열 존재하지 않으면 -1 출력
"""

"""
시간초과남 - 로직 수정 --> 근데 걍 import sys 이거 문제 였음..
1. bfs로 시작점 ~ 모든 도시까지의 최단 거리를 구한 뒤
    - 현재 도시에서 이동할 수 있는 모든 도시를 확인(인접 노드)
    - 각 도시에 대해, 방문하지 않은 도시라면, 최단 거리 갱신
2. 그 값이 K인 경우에 해당 도시 번호 출력
"""

from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M) :
    x, y = map(int, input().split())
    graph[x].append(y)


def bfs(v) :
    out = []
    min_dist = [-1] * (N+1)
    min_dist[v] = 0

    que = deque([v])

    while que: 
        cur = que.popleft()
        for g in graph[cur] :
            if min_dist[g] == -1:
                min_dist[g] = min_dist[cur] + 1
                que.append(g)
    
    for i in range(1, N+1) :
        if min_dist[i] == K :
            out.append(i)
    
    return out

output = bfs(X)
if not output : print(-1)
else : 
    output.sort()
    for o in output : print(o)