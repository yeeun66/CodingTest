# DFS와 BFS
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램

# from collections import deque

n, m, v = map(int, input().split()) # vertex, edge, start vertex

# matrix 0으로 초기화
def init_matrix(a, b) :
    matrix = []
    for i in range(a) :
        row = []
        for j in range(a) :
            row.append(0)
        matrix.append(row)
    # 입력 m개 받아서 matrix에 2m개 1로 변경
    for i in range(b) :
        x, y = map(int, input().split())
        matrix[x-1][y-1] = 1
        matrix[y-1][x-1] = 1
    return matrix

# DFS
def dfs(matrix) : 
    dn = n
    dv = v
    dfs_matrix = matrix
    flag = [0] * dn
    # start vertex 부터 출력 후 stack에 저장
    dfs = [] # 출력 리스트
    dfs.append(dv)
    flag[dv-1] = 1
    stack = []
    stack.append(dv)
    cv = dv-1 # 현재 vertex
    while len(dfs) != dn :
        p = 0
        while p != 1 :
            j = 0
            while j < dn :
                if dfs_matrix[cv][j] == 1 and flag[j] != 1 :
                    dfs.append(j+1)
                    stack.append(j+1)
                    flag[j] = 1
                    p = 1
                    cv = j
                    break
                j += 1
            if p != 1 : 
                if len(stack) != 0 :
                    stack.pop()
                    if len(stack) != 0 : 
                        cv = stack[-1] -1
    return dfs

# BFS
def bfs(matrix) :
    bn = n
    bv = v
    bfs_matrix = matrix
    flag = [0] * bn
    # start vertex 부터 출력 후 queue에 저장
    bfs = [] # 출력 리스트
    bfs.append(bv)
    flag[bv-1] = 1
    queue = []
    queue.append(bv)
    cv = bv-1 # 현재 vertex
    while len(bfs) != bn :
        j = 0
        while j < bn :
            if bfs_matrix[cv][j] == 1 and flag[j] != 1 :
                bfs.append(j+1)
                queue.append(j+1)
                flag[j] = 1
            j += 1 
        if len(queue) != 0 :
            queue.pop(0)
            if len(queue) != 0 : 
                cv = queue[0] -1
    return bfs

# 출력
matrix = init_matrix(n, m)
print_dfs = dfs(matrix)
print_bfs = bfs(matrix)
for i in range(n) :
    print(print_dfs[i], end=' ')
print()
for i in range(n) :
    print(print_bfs[i], end=' ')