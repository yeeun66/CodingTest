# 숨바꼭질 2
# 가장 짧은 시간과 그 방법이 몇가지인지 구하기

# 그냥 원래 숨바꼭질 로직에서, 발견하면 바로 리턴하지 말고, 카운트 함
    # 이때 카운트하고는 컨티뉴 해줘서 아래 로직 실행 안되도록 해야함. 발견 이후로 또 찾을 이유가 없기 때문
# 그리고 최초 방문, 즉 graph == 0 일때는 당연히 큐에 넣지만
# 재방문 시에는 현재 값이 다음 갈 곳과 1 차이이면, 즉 최단 거리임이 보장되면, 큐에 넣어서 동생 찾을 준비를 함

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
graph = [0] * (1000001)

def bfs() : 
    cnt = 0

    queue = deque()
    queue.append(N)

    while queue : 
        cur = queue.popleft()
        if cur == K : 
            cnt += 1 # 방금 pop한 것이 동생이면 카운트
            continue

        for i in range(3) :
            if i == 0 : n = cur+1
            elif i == 1 : n = cur-1
            else : n = cur*2

            if 0 <= n < 1000001 : 
                if graph[n] == 0 : 
                    graph[n] = graph[cur] + 1
                    queue.append(n)
                elif graph[n] == graph[cur] + 1 : # 다음 갈 곳이 현재 갈 곳과 한 개 차이이면, 즉 최단거리면
                    queue.append(n)

    print(graph[0:30])
    print(graph[K])
    print(cnt)

if N == K : 
    print(0)
    print(1)
    exit()

bfs()