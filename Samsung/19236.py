# 청소년 상어

# 0. 필요한 변수
    # 방향 이동을 위한 변수 dx, dy 8가지 방향 표현
    # fishes 배열 (크기 17, 1번~16번 사용) 
        # 초기 입력인 16개 물고기에 대하여 한 물고기 당 (번호, 방향, 좌표) 총 4가지 원소 저장
            # 이 때, (0, 0)은 상어 입장 때문에 shark에 저장
                # 근데 fishes에도 저장은 해두는데, fishes[해당 번호][-1, 0, 0]으로 저장
    # arr 배열
        # 현재 번호를 올바른 위치에 저장 해둠
        # 나중에 좌표로 꺼내고 교환할 때 사용

# 1. fishes 오름 차순으로 정렬 후 이동 (1번 물고기 부터~)
    # 1-1. 이동 가능한지 확인
        # nd = d를 저장
        # nd를 이용해 nx, ny 를 업데이트 하며,
            # 이동하려는 칸에 상어가 있으면, 즉 fishes[해당 번호][0] == -1이면 이동 불가
                # 그리고 경계 넘어가도 이동 불가
                # 이동 불가이면, 방향 바꿔줌 nd = (nd + 1) % 9
            # 나머지 경우는 다 이동 가능
    # 1-2. 이동 또는 이동 안하기
            # 이동 가능하면
                # 이동할 곳에 있는 물고기의 번호 알아냄.
                # 방금 알아낸 번호로 인덱스 접근하여 좌표 교환 
                    # 만약 arr[nx][ny] = 2라면, 
                    # fishes[2][1], fishes[2][2] = x, y
                # 현재 물고기도 정보 바꿔줌 fishes[현재] = [nd, nx, ny]
                # arr에도 교환한 번호로 값 바꿔줌 
            # 이동 8번 다했는데 이동할 곳 없으면, 아무일도 X

# 2. 상어 이동 (DFS로 구현)
    # shark에 저장된 방향에 대해, 갈 수 있는 칸이 있을 건데, 
        # 이 칸들을 중 하나 방문 했다 치고, 계속 dfs로 들어가서
        # 상어 종료시 까지, 즉 상어가 이동할 수 있는 칸 없을 때 까지 반복
        # 재귀 빠져나오면, 다시 원상 복귀 시키기 위해 재귀 들어가기 전, deep copy로 배열 두개 복사해두기

from copy import deepcopy

dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

fishes = [[] for _ in range(17)] # [방향, x좌표, y좌표]
fishes[0] = [0, 0, 0]

arr = [[0]*4 for _ in range(4)]

# 입력
for i in range(4):
    tmp = list(map(int, input().split()))
    jdx = 0
    for j in range(4):
        if i == 0 and j == 0:
            fishes[tmp[jdx]] = [-1, 0, 0]
            shark = [tmp[jdx], tmp[jdx+1], 0, 0]  # 번호, 방향, 좌표 (x, y)
        else:
            fishes[tmp[jdx]] = [tmp[jdx+1], i, j]
            arr[i][j] = tmp[jdx]
        jdx += 2

def move_fish(arr, fishes):
    arr = deepcopy(arr)
    fishes = deepcopy(fishes)
    for i in range(1, 17):
        d, x, y = fishes[i][0], fishes[i][1], fishes[i][2]
        if d == -1:
            continue

        for k in range(8):
            nd = (d + k) % 8
            if nd == 0: nd = 8
            nx, ny = x + dx[nd], y + dy[nd]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if arr[nx][ny] != -1:
                    num = arr[nx][ny]
                    fishes[i] = [nd, nx, ny]
                    fishes[num][1], fishes[num][2] = x, y
                    arr[x][y], arr[nx][ny] = num, i
                    break
    return arr, fishes

def dfs(d, x, y, result, arr, fishes):
    global max_result
    max_result = max(max_result, result)

    arr, fishes = move_fish(arr, fishes)

    for i in range(1, 4):
        nx = x + dx[d] * i
        ny = y + dy[d] * i

        if 0 <= nx < 4 and 0 <= ny < 4 and arr[nx][ny] > 0:
            new_arr, new_fishes = deepcopy(arr), deepcopy(fishes)

            eat_num = new_arr[nx][ny]
            eat_d = new_fishes[eat_num][0]

            new_arr[x][y] = 0
            new_arr[nx][ny] = -1
            new_fishes[eat_num][0] = -1

            dfs(eat_d, nx, ny, result + eat_num, new_arr, new_fishes)

max_result = 0
arr[0][0] = -1
fishes[shark[0]][0] = -1
dfs(shark[1], 0, 0, shark[0], arr, fishes)

print(max_result)