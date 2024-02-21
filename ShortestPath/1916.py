# 최소비용 구하기
# N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다. 
# 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. 
# A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.
# 출발도시, 도착지, 비용
# 마지막 줄 : 출발점의 도시번호, 도착점의 도시번호 (출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어짐)

# 이것도 그냥 다익스트라 알고리즘

# 아니 틀렸다고 뜨는데 왜 틀린거지. 틀린 반례가 없는데 -> 최단 거리 테이블에 float("INF")로 바꾸고 해결함
# 간선이 최대 100000개에 가중치가 최대 100000이면 이론상 10^10까지 가능 ???
import sys
import heapq
input = sys.stdin.readline

V = int(input())
E = int(input())

distance = [float("INF")] * (V+1) # 최단 거리 테이블 <-- 이거 수정하고 해결
graph = [[] for _ in range(V + 1)]

for _ in range(E) :
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start)) # 비용, node 번호 순으로 넣기
    distance[start] = 0
    while queue :
        dist, num = heapq.heappop(queue)
        if distance[num] < dist : 
            continue
        for i in graph[num] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0])) 

start, target = map(int, input().split())

dijkstra(start)

print(distance[target], end="")