# 마법사 상어와 파이어스톰

# 큰 로직
    # 1. 부분 격자에 대해 시계 방향 회전 rotate_90()
    # 2. 얼음의 양 1 줄어든다
    # 3. 2가지 구하기
       # 1) 남아 있는 얼음 A[r][c]의 합
       # 2) 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수 - BFS 하며, 최대값 업데이트
# 세부 로직
    # 1. 부분 격자에 대해 시계 방향 회전 rotate_90()
        # 임시 배열 new_arr (arr과 같은 크기) 생성
        # 4중 반복문으로 회전할 구간 정해 놓고 회전 시킨 다음 바로 적용.
        # 1, 2 중 반복은 구간 시작점
        # 3, 4 중 반복은 구간 내에서 회전할 위치 시작점
        # 90도 회전
        # new_arr[i][j] = arr[(n-1)-j][i]

    # 2. 얼음의 양 -1 / count_ice()
        # 임시 배열 new_arr (arr과 같은 크기) 생성
        # 모든 위치에 대하여
            # 인접 칸 탐색, 주변 얼음 수 카운트
            # 카운트 3개 미만이면 해당 칸 얼음양 -1
            # 아니면 얼음양 그대로
        # new_arr을 리턴

    # 3. 2가지 구하고 출력
        # 얼음의 합은 어렵지 않음
        # 가장 큰 덩어리의 칸 개수 - BFS()하며 최대값 업데이트

# 사용 배열 arr, sub_arr, level

from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

N, Q = map(int, input().split())
arr = []
for _ in range(2**N) : arr.append(list(map(int, input().split())))

level = list(map(int, input().split()))
total = 2**N

def rotate_90(old_arr, l) :
    sub = 2 ** l
    new_arr = [[0]*total for _ in range(total)]

    for i in range(0, total, sub) :
        for j in range(0, total, sub) :
            for a in range(sub) :
                for b in range(sub) :
                    new_arr[i+a][j+b] = old_arr[i+(sub-1-b)][j+a]

    return new_arr

def count_ice(old_arr) :
    new_arr = [[0] * total for _ in range(total)]

    for i in range(total) :
        for j in range(total) :
            if old_arr[i][j] > 0 :
                cnt = 0
                for k in range(4) :
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < total and 0 <= ny < total :
                        if old_arr[nx][ny] > 0 : cnt += 1

                if cnt < 3 : new_arr[i][j] = old_arr[i][j] - 1
                else : new_arr[i][j] = old_arr[i][j]

    return new_arr

def bfs(x, y) :
    cnt = 1
    que = deque()
    que.append((x, y))
    while que :
        x, y = que.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < total and 0 <= ny < total and not visited[nx][ny] and arr[nx][ny] > 0:
                visited[nx][ny] = 1
                que.append((nx, ny))
                cnt += 1

    return cnt


######## main ########
for i in range(Q) :
    arr = rotate_90(arr, level[i]) # 1. 부분 격자 회전
    arr = count_ice(arr) # 2. 얼음의 양 -1

# 3. 2가지 구하고 출력
print(sum([sum(a) for a in arr])) # 1) 얼음의 합

max_v = 0 # 2) 덩어리 최대 갯수
visited =  [[0] * total for _ in range(total)]

for i in range(total) :
    for j in range(total) :
        if not visited[i][j] and arr[i][j] > 0 :
            visited[i][j] = 1
            tmp = bfs(i, j)
            max_v = max(tmp, max_v)

print(max_v)