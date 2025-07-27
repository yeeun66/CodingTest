# DFS 스페셜 저지
# 올바른 DFS 방문 순서인지 구하기
'''
1. 우선 DFS 한번 돌리면서 부모-자식 관계 파악해두기
2. 백트래킹으로 모든 경우의 수 output에 담아두기
3. test가 output에 있는지 검사
'''
# N = int(input())
# graph = [[] for _ in range(N+1)]
# for _ in range(N-1) : 
#     x, y = map(int, input().split())
#     graph[x].append(y)
#     graph[y].append(x)

# test = list(map(int, input().split()))

# child = [[] for _ in range(N+1)]
# check = [False] * (N+1)
# def dfs(x) :
#     if check[x] == True : return

#     check[x] = True
#     for y in graph[x] :
#         if not check[y] : 
#             print('y: ', y)
#             child[x].append(y)
#             dfs(y)

# '''
# 그냥 test에서 0번 부터 시작해서 아래를 검사
# st = 1부터 시작. 
# 현재 값이 리프 노드이면, 리프 노드가 아닐 때 까지 cur -= 1, 
#     - 반복 끝나면 st += 1
# 리프 노드가 아닐 때, 
#     - st에 있는 값이 자기 자식이면 cur = st, st += 1 하고 그 값은 지워 
#     - st에 있는 값이 자기 자식이 아니면 0 출력 후 종료

# 끝나면 1 출력
# '''

# st = 1
# for t in test :
#     cur = t
#     if not child[cur] : 
#         while not child[cur] :
#             cur -= 1
    
#     else :
#         if test[st] in child[cur] :
#             cur = st
            
    

# dfs(1)
# print(child)
# arr = [1]
# check_dfs(1)
# print(output)
