# 특정한 최단 경로
# 방향성이 없는 그래프. 1번 정점에서 N번 정점으로 최단 거리로 이동
# 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다.

# 1번 정점에서 N번 정점으로 이동할 때, (조건) 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램
# 예상시간: 1시간 / 소요시간: 2시간

# 다익스트라 알고리즘 + 조건 체크 끝날 때까지 반복
# 조건 처리 로직: 
    # case 2개로 나눠서 둘 중 최소 선택해서 출력
    # case1 -> 1 - v1 - v2 - V 순으로 가는 경우    
    # case2 -> 1 - v2 - v1 - V 순으로 가는 경우
    # => a번째 노드부터 b번째 노드까지가는 최단 거리 구하는 걸 저 원소들로 한 경우당 세번씩 수행해서 합해주기
    #    (즉 다익스트라 함수 총 6번 호출)
    #    그럼 합한 값 두 개 나오겠지. 그거 둘 중 최소값 출력

# 반례1) 간선이 존재하지 않을 때 -1 출력하도록 고려해야 함 -> 해결
# 반례2) v1 = V 이거나, v2 = N 인 경우 -> 해결
# 반례3) answer가 여전히 inf 인경우 -1 출력하도록 -> 해결
import sys
import heapq as hq

input = sys.stdin.readline
V, E = map(int, input().split()) # 0 ≤ E ≤ 200,000

graph = [[] for _ in range(V+1)]
for _ in range(E) :
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

v1, v2 = map(int, input().split()) # v1 ≠ v2, v1 ≠ N, v2 ≠ 1

a = [1, v1, v2, V] # case1
b = [1, v2, v1, V] # case2

def dijkstra(st, end) :
    distance = [float("INF")] * (V+1)
    que = []
    hq.heappush(que, (0, st))
    distance[st] = 0
    while que :
        dist, num = hq.heappop(que)

        if dist > distance[num] : continue
        for new_num, new_dist in graph[num] :
            cost = dist + new_dist
            if cost < distance[new_num] :
                distance[new_num] = cost
                hq.heappush(que, (cost, new_num))
    return distance[end]
    
sum = [0] * 2
for i in range(3) : 
    if a[i] == a[i+1] : continue
    sum[0] += dijkstra(a[i], a[i+1])

for i in range(3) : 
    if b[i] == b[i+1] : continue
    sum[1] += dijkstra(b[i], b[i+1])

answer = min(sum[0], sum[1])
if answer == 0 or answer == float("INF") : print(-1)
else : 
    print(answer)