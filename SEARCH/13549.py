# 숨바꼭질 3
# 그냥 원래 숨바꼭질 로직에서, 순간이동시에만 방문처리 +1 하지 않고 그냥 부모 방문 기록으로 하면 될듯
from collections import deque
N, K  = map(int, input().split())
graph = [0] * 100001

def bfs() :
    que = deque([N])
    while que : 
        cur = que.popleft()

        for i in range(3) :
            if i == 0 : n = cur*2
            elif i == 1 : n = cur-1
            else : n = cur+1

            if 0<= n < 100001 :
                if graph[n] == -100 :
                    if i != 0 : return (graph[cur] + 1)
                    else : return graph[cur]
                elif graph[n] == 0 :
                    if i != 0 : graph[n] = graph[cur] + 1
                    else : graph[n] = graph[cur]
                    que.append(n)
if N == K : 
    print(0)
    exit()
    
graph[N] = 0
graph[K] = -100
print(bfs())