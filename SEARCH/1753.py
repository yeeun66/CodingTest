# 최단경로 -- 해결
# 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램

# 다시 짜
# 우선순위큐로 변경, w값 업데이트(dp처럼 table 생성)
# 모든 노드마다 최단 경로가 가중치로 들어가게끔 해서 그걸 출력
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9) # 무한을 의미하는 값. 10억을 설정

# 노드의 개수, 간선 개수
n, m = map(int, input().split())
# 시작 노드
start = int(input())

graph = [[] for i in range(n + 1)]

# !!! 최단 거리 테이블!!! <- 이게 중요한 개념. 모두 무한으로 초기화
distance = [INF] * (n + 1)

for _ in range(m):
    #출발, 도착, 가중치
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 그래프랑 큐랑 (노드번호, 가중치) 삽입되는 순서 다르다는 거 헷갈리지 않기! (같게 만들어줘도 되긴 함)
def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start)) # 비용, node 번호 순으로 넣기
    distance[start] = 0
    while queue: 
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(queue)
        # 현재 노드가 이미 처리된 적이 있는 노드면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드들 확인
        for i in graph[now]:
            cost = dist + i[1] # pop한 비용 + 그래프에 있던 비용
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
        print(queue)

# print(graph)
dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF: 
        print("INF")
    else: 
        print(distance[i])