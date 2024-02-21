# 특정 거리의 도시 찾기

# 방향 그래프, 모든 가중치=1
# 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램
# 기존 다익스트라 알고리즘 사용 후, 최단 거리 테이블의 값이 K이면, 노드 번호 출력
# 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력

import sys
import heapq as hq

input = sys.stdin.readline

V, E, K, X = map(int, input().split())

distance = [float("INF")] * (V+1) # 최단거리 테이블

graph = [[] for _ in range(V+1)]
for _ in range(E) :
    u, v = map(int, input().split())
    graph[u].append((v, 1))

def dijkstra(start):
    queue = []
    hq.heappush(queue, (0, start))
    distance[start] = 0

    while queue :
        dist, num = hq.heappop(queue)

        for new_num, new_dist in graph[num] :
            cost = dist + new_dist
            if cost < distance[new_num] :
                distance[new_num] = cost
                hq.heappush(queue, (cost, new_num))


dijkstra(X)

flag = 0
for i in range(1, V+1) :
    if distance[i] == K :
        flag = 1
        print(i)
if flag == 0 : print(-1)