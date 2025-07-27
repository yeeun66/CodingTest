# 이분 그래프 
'''
이분 그래프 (Bipartite Graph) : 인접한 정점끼리 서로 다른 색으로 칠해서 모든 정점을 두 가지 색으로만 칠할 수 있는 그래프. 
즉, 같은 그룹(= 같은 level)에 속한 정점끼리는 서로 인접하지 않도록 하는 그래프 
'''

'''
이분 그래프 판별 로직: bfs, dfs 둘 다 가능
bfs 로직
1. bfs로 탐색한다
2. 탐색 중 인접 노드에 대해 
    - 아직 방문 전이면, 자신과 다른 색을 부여 (빨강: 1, 파랑 -1)
    - 이전에 방문 되었을 때, 자신과 같은 색을 가지고 있다면, 이분 그래프가 아님 - 바로 NO 리턴
3. 모두 탐색 후 YES 리턴 

** 처음에 고려 안한 것 : 비연결 그래프도 고려해야함.
1부터 탐색할 경우, 1과 아예 연결되어 있지 않은 노드들은 탐색안하고 YES가 되어버림.
그래서 bfs 끝났을 경우에도 아직 방문하지 않은 노드들 방문하도록 다시 bfs 돌려주기
'''

from collections import deque
K = int(input())

def all_visit(visit) :
    for i in range(1, V+1) : 
        if visit[i] == 0 : return i
    
    return 0

def bfs() :
    visited = [0] * (V+1)
    que = deque([1])
    visited[1] = 1 # Red

    while True : 
        while que : 
            cur = que.popleft()
            for g in graph[cur] : 
                if not visited[g] : 
                    visited[g] = visited[cur] * (-1) # 다른색 부여
                    que.append(g)
                else : 
                    if visited[g] == visited[cur] : return 'NO'

        flag = all_visit(visited) # 비연결 그래프 고려
        if not flag : break 
        visited[flag] = 1
        que = deque([flag])
    
    return 'YES'

for _ in range(K) :
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E) :
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    print(bfs())