# BFS 스페셜 저지
# 부모 자식 관계 중요!!
# 처음에 틀렸던 로직은 depth만 제대로 되었는지 고려하고 부모-자식 관계 고려 안함
    # 그럼 이런거 틀림
    '''
    5
    1 2
    2 5
    1 3
    3 4
    1 2 3 4 5
    '''

'''
** 부모 자식 관계 체크 (부모-자식 간의 순서는 상관 없으니 set으로 저장 함)
graph 2차원 리스트에 인접 노드 저장 
    Ex) graph = [[], [2, 3], [1, 5], [1, 4], [3], [2]]
1. bfs 수행
    - 1부터 큐에 넣음 
    - popleft 후, 인접 리스트들 중 방문 안한거 방문처리 후 큐에 추가
    - 1이 아니면 child 배열에 부모-자식 관계 추가하기 
        ex) child[1] = (2, 3) # 2와 3의 부모는 1
2. bfs 올바른지 체크 
    - test의 0번째 배열부터 검사 시작
    - st = 1부터 시작, 
        - tmp = [st: st+len(child(t))]
        - tmp와 child가 다르면 자식 관계 아닌 것. 0 출력 후 종료
        - st = st+len(child(t)) .. 계속

여기까지 오면 1 출력
'''
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1) :
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

test = list(map(int, input().split()))

# bfs 
child = [set() for _ in range(N+1)]
visited = [0] * (N+1)
que = deque([1])
visited[1] = 1
while que : 
    n = que.popleft()
    for g in graph[n] :
        if not visited[g] :
            visited[g] = 1
            child[n].add(g)
            que.append(g)

# check
st = 1
for t in test : 
    length = len(child[t])
    tmp = test[st: st+length]
    if set(tmp) != child[t] :
        print(0)
        exit()
    st += length

print(1)