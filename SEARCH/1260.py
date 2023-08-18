# DFS와 BFS
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램
n, m, v = map(int, input().split()) # vertex, edge, start vertex

# matrix, flag 0으로 초기화
matrix = []
flag = [0] * n
for i in range(n) :
    row = []
    for j in range(n) :
        row.append(0)
    matrix.append(row)
# 입력 m개 받아서 matrix에 2m개 1로 변경
for i in range(m) :
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    matrix[x][y] = 1
    matrix[y][x] = 1
# start vertex 부터 출력 후 stack에 저장
print_bfs = [] # 출력 리스트
print_bfs.append(v)
flag[v-1] = 1
stack = []
stack.append(v)
cv = v-1 # 현재 vertex
while len(print_bfs) != n :
    p = 0
    while p != 1 :
        j = 0
        while j < n :
            if matrix[cv][j] == 1 and flag[j] != 1 :
                print_bfs.append(j+1)
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

for i in range(n) :
    print(print_bfs[i], end=' ')

# DFS

# BFS