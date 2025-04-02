# 마법사 상어와 비바라기
# 5:00 

# 로직
# 1. 입력 받기, 배열 생성
    # N*N 의 격자 배열 arr에 입력받기
    # cloud deque 생성 후, 초기 구름 append
    #   (N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1) 
    # 명령은 2차원 배열 cmd에 입력 받기

# 2. cmd에서 하나씩 꺼내며 다음을 반복
    # 2-1. 모든 구름이 d 방향으로 s칸 이동한다.
    # cloud에서 하나씩 꺼내서 pop
        # nr = (r + s*dx[d] + N) % N
        # nc = (c + s*dy[d] + N) % N
        # cloud에서 왼쪽으로 (nr, nc) append
    # 2-2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
        # cloud에 있는 좌표 각 칸에 대하여 arr[r][c] 값 1증가
    # 2-3.물이 증가한 칸 (r, c)에 물복사버그 마법을 시전
        # 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)바구니의 물의 양 증가 시키기
        # 대각선으로 상하좌우 탐색 (대각선은 2, 4, 6, 8 즉 짝수 dx dy)
            # 이 때 nr, nc는 격자 경계 빠져나가면 안됨
            # 경계 안에서, arr[nr][nc] 값이 1이상이면 카운트
        # 탐색한 카운트 만큼 현재 (r, c)에 물 증가 시킴 arr[r][c] += cnt
        # (추가로) 초기화 직전에, 이 좌표들 임시 배열에 좌표 넣어두기 (5번 때문에) <- 이거 set으로 해야 함
    # 2-4. 구름 모두 사라짐 cloud.clear()
    # 2-5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어듦
        # 모든 arr 배열 칸에 대해,
            # 4번에서 만든 좌표에 속하지 않고, 값이 2이상인 칸에 대해,
                # cloud에 추가하고 arr 값은 2 줄어든다.

# 3. sum(arr) 출력

# 시간 초과.. 
# 해결 >> not in 하기 위한 tmp_cloud 배열을 set으로 변경 (이거 아주 중요!!)

from collections import deque
# 방향: 1 2 3 4 5 6 7 8 (0번 일부러 안씀)
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

N, M = map(int, input().split())
arr = []
for _ in range(N) : arr.append(list(map(int, input().split())))
command = []
for _ in range(M) : command.append(list(map(int, input().split())))
cloud = deque() # 여기에 좌표로 저장

# 초기 구름 설정
cloud.append((N-1, 0))
cloud.append((N-1, 1))
cloud.append((N-2, 0))
cloud.append((N-2, 1))

for cmd in command :
    d, s = cmd

    for _ in range(len(cloud)) :
        # 끝에꺼 빼서 앞에 넣으면서 구름 이동
        r, c = cloud.pop()
        nr = (r + s*dx[d] + N) % N
        nc = (c + s*dy[d] + N) % N
        cloud.appendleft((nr, nc))
   
    # 2. 구름 비내려서 물 증가
    for cld in cloud : 
        r, c = cld
        arr[r][c] += 1

    # 3. 물복사버그 마법을 시전
    tmp_cloud = set() # not in 같은거 할 때 set 써야 시간복잡도 빠름!!
    for cld in cloud : 
        r, c = cld
        tmp_cloud.add((r, c))
        cnt = 0
        for k in range(1, 5) : # 대각선 카운트
            nr = r + dx[2*k]
            nc = c + dy[2*k]
            if 0<= nr <N and 0<= nc <N and arr[nr][nc] > 0: cnt += 1
        arr[r][c] += cnt

    # 4. 구름 모두 사라짐 
    cloud.clear()

    # 5. 구름 다시 생성
    for r in range(N) : 
        for c in range(N) : 
            if arr[r][c] >= 2 and (r, c) not in tmp_cloud:
                cloud.append((r, c))
                arr[r][c] -= 2
    
result = 0
for a in arr : result += sum(a)
print(result)