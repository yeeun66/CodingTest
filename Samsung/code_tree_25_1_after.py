"""
코드 트리 - 미생물 연구
아주 오래 걸림 (하루 이상)
근데 생각을 잘못한거였음
가장 왼쪽으로 간 후에 가장 위쪽으로 가는게 아니라,
모든 평행이동 가능한 위치 중에서, 가장 좌상단 좌표를 뽑으면 되는거였음!!

1. N, Q 그리고 각 미생물 정보 입력 받기 (creature 배열)
    (r1, c1, r2, c2) - 좌측 하단, 우측 상단
    주의** r이 열이고 c가 행이다

아래 2~4를 Q번 반복
2. 미생물 투입 - creature_insert()함수
    1) (r1, c1, r2, c2)인 영역에 미생물을 투입함
        creature_size 에 정보 저장 -> creature_size[1]은 1번 미생물의 영역 넓이
        투입하려는 칸에 0이 아닌 값이 있다면 (다른 미생물 이미 존재) 그 값은 잡아 먹힘 - 잡아 먹힌 미생물 숫자 기록 (eaten 배열)
            잡아 먹힐 때마다 해당 creature_info[해당 번호] -= 1
    2) 잡아 먹힌 미생물이 있을 때, 해당 미생물의 영역이 둘 이상으로 분리 되었는지 확인 - bfs()
            분리 되었다면, 해당 미생물 용기에서 모두 제거 - 0으로 변경

3. 배양 용기 이동 (기존 배양 용기 빌 때까지 반복) - move_arr()
    1) 옮길 미생물 종류 우선 순위 정하기
        영역 큰 순 > 먼저 투입된 순

    2) 선택된 각 미생물 무리를 새 배양 용기로 이동

        (2-1) 현재 위치 파악 및 "모양 추출”
            - 현재 배양 용기에서 해당 미생물이 차지한 모든 좌표를 `positions`에 저장
            - 좌상단 기준으로 상대 좌표로 바꿔서 모양을 추출

        (2-2) 이동 가능한 모든 위치 탐색
            - 해당 모양을 그대로 이동시켜도 겹치지 않는 위치를 모두 찾음
                - `candidates`에 모든 가능한 위치 저장
            - 이때`candidates`에는 `(j, i)` 순서로 저장해서 열 우선(왼쪽 위 기준) 정렬이 되도록 함

        (2-3)  가장 왼쪽 위 위치에 배치
            - 가능한 위치들 중에서 가장 왼쪽 위 좌표를 선택함 (오름차순 정렬로 0번째 좌표)
            - 선택된 좌표에 그대로 배치 (상대좌표 + 선택된 좌표)

        (2-4) 둘 곳이 없는 미생물은 제거
            - creature_size[selected_num] = 0

4. 실험 결과 기록 - report_result()
    1) 인접한 무리 계산 - bfs()
        중복되지 않도록 set에 추가 (1번 2번이 인접해 있으면 neighbor에 [1,2]를 추가)
    2) neighbor에 추가된 무리에 대해서 성과 얻기
        실험 결과 += 1의 영역 넓이 X 2의 영역 넓이
    3) 실험 결과 출력
"""

from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, Q = map(int, input().split())
creature = []
for _ in range(Q) : creature.append(list(map(int, input().split())))
arr = [[0 for _ in range(N)] for _ in range(N)] # 기존 배양 용기
creature_size = [0 for _ in range(Q+1)] # 각 미생물 당 현재 영역 크기 저장

def bfs(x, y, visited) :
    que = deque()
    que.append((x,y))
    visited[x][y] = True
    num = arr[x][y]
    adj = [] # 인접 미생물 번호 저장

    while que:
        x, y = que.popleft()
        for i in range(4) :
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                if arr[nx][ny] == num:
                    que.append((nx, ny))
                    visited[nx][ny] = True
                elif arr[nx][ny] > num: adj.append(arr[nx][ny])

    adj = set(adj) # 중복 제거

    return visited, adj

def creature_insert(c, num):

    eaten = set() # 잡아 먹힌 미생물 기록
    r1, c1, r2, c2 = c  # 이번에 투입할 미생물
    creature_size[num] = (c2-c1) * (r2-r1)
    for i in range(c1, c2) :
        for j in range(r1, r2) :
            if arr[i][j] != 0 :
                eaten.add(arr[i][j])
                creature_size[arr[i][j]] -= 1
            arr[i][j] = num

    while eaten : # 잡아 먹힌 미생물이 있을 때, 해당 미생물의 영역이 둘 이상으로 분리 되었는지 확인 - bfs()
        n = eaten.pop()
        cnt = 0 # 분리 영역 확인
        visited = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if arr[i][j] == n and not visited[i][j]:
                    visited[i][j] = True
                    visited, _ = bfs(i, j, visited)
                    cnt += 1
                if cnt >= 2 : break
            if cnt >= 2: break

        if cnt >= 2 : # 분리 되었다면, 해당 미생물 용기에서 모두 제거 (0으로 변경)
            creature_size[n] = 0 # 크기도 0으로 변경
            for i in range(N):
                for j in range(N):
                    if arr[i][j] == n : arr[i][j] = 0

def move_arr(num): ## 중요! 가능한 모든 곳을 다 살펴보고, 그중 가장 "왼쪽 위에 가까운" 곳을 고르기!!
    new_arr = [[0 for _ in range(N)] for _ in range(N)]

    # 1) 옮길 미생물 종류 우선 순위 정하기
    priority = [] # 배양 용기에 넣을 무리 순서 정하기
    for i in range(1, num + 1):
        if creature_size[i] > 0:
            priority.append((-creature_size[i], i))  # 큰 크기 우선, 번호가 빠를수록 우선

    priority.sort()

    # (2-1) 현재 위치 파악 및 "모양 추출
    for _, selected_num in priority:
        positions = []
        for i in range(N):
            for j in range(N):
                if arr[i][j] == selected_num:
                    positions.append((i, j))

        # 좌상단 기준으로 상대 좌표로 바꿔서 모양을 추출
        min_x = min(x for x, y in positions)
        min_y = min(y for x, y in positions)
        shape = [(x - min_x, y - min_y) for x, y in positions] # 해당 무리의 모든 좌표에 대해 가장 좌상단으로 이동

        # (2-2) 이동 가능한 모든 위치 탐색
        candidates = [] # 모양 유지하며, 이동할 수 있는 모든 위치들

        for i in range(N):
            for j in range(N):
                can_place = True
                for dx_, dy_ in shape:
                    nx, ny = i + dx_, j + dy_ # 모든 좌표 탐색
                    if not (0 <= nx < N and 0 <= ny < N) or new_arr[nx][ny] != 0: # 범위 벗어나거나, 다른 미생물이 있으면
                        can_place = False # 놓을 수 없는 위치
                        break
                if can_place: # 놓을 수 있는 위치 라면
                    candidates.append((j, i))  # 열 우선 정렬을 위해 (x, y) → (j, i)

        # (2-3)  가장 왼쪽 위 위치에 배치
        if candidates:
            candidates.sort()
            best_j, best_i = candidates[0] # 가능한 위치 중 가장 좌상단 좌표
            for dx_, dy_ in shape:
                nx = best_i + dx_
                ny = best_j + dy_
                new_arr[nx][ny] = selected_num
        else:
            creature_size[selected_num] = 0

    return new_arr

def report_result(num):
    neighbor = []
    result = 0
    for n in range(1, num) : # 1~num 까지의 미생물에 대해 인접 무리 계산
        visited = [[0 for _ in range(N)] for _ in range(N)]
        adj = []  # 인접 미생물 번호 저장
        for i in range(N) :
            for j in range(N):
                if arr[i][j] == n and not visited[i][j] :
                    visited, adj = bfs(i, j, visited)

        for ad in adj:
            if [ad, n] not in neighbor : neighbor.append([n, ad])

    for a, b in neighbor : result += creature_size[a] * creature_size[b]

    print(result)


##### Main #####
for q in range(Q) :

    creature_insert(creature[q], q+1) # 1. 미생물 투입

    arr = move_arr(q+1) # 2. 배양 용기 이동

    creature_size = [0 for _ in range(Q + 1)] # move 후 creature_size 재계산
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                creature_size[arr[i][j]] += 1

    ### 디버깅 중 #####
    # print('#'* 10, q + 1)
    # for a in arr: print(a)
    ### 디버깅 중 #####

    report_result(q+1)  # 3. 실험 결과 출력