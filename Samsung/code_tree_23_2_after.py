# 코드트리 - 루돌프의 반란
# 4시간 이상 걸렸는데도 틀림. 해설 참고해서 정답 맞춤
"""
<기본 정보 정리>
    산타 정보 나타내는 배열
        - position, is_live, stopped, score 로 구분 해서 정보 분산
    arr에 루돌프는 -1로, 빈칸은 0, 산타의 번호 1~P+1
<함수 정리>
    is_range(x, y) : x, y가 보드 내의 좌표인지 확인하는 함수 => 이거 쓰면 코드가 깔끔해짐
<로직 정리>
1. 루돌프 이동 -> 충돌
    1-1) 살아있는 산타 중 루돌프에 가장 가까운 산타 찾기
        모든 산타에 대해 거리 체크 (루돌프와의 거리 가장 짧고 그중에서는 행과 열이 큰 산타 하나 찾기)
    1-2) 산타 찾았으면 (== 갈 곳 있으면) 그곳으로 루돌프 이동
        -> 이 때 현재 루돌프 위치와 가까운 산타의 행과 열 크기 비교해서
            행과 열을 증가할지 감소할지 결정
    1-3) 루돌프의 이동으로 충돌한 경우 처리
        가까운 산타랑 지정된 좌표가 루돌프와 같다면 (=충돌)
            c만큼 산타 밀어내고 산타는 점수 얻고나서 기절 또는 탈락 할건데,
            여기서 산타가 밀어내진 칸에 다른 산타가 있다면 연쇄 이동이 일어남
                연쇄 이동시, 루돌프와 충돌한 산타 말고 다른 애들은, 탈락 시키거나 이동 시킴
            충돌한 산타는 밀려난 위치가 경계 밖이면, 탈락 처리
            경계 안이면, 이동 처리 (arr 업데이트)
        루돌프 arr에 표시 -1

2. 산타들의 이동 -> 충돌
    각 산타들에 대해 아래를 수행
    2-1) 산타들은 루돌프와 가장 가까운 방향으로 한칸 이동
        이때 현재 위치보다 멀어지는 이동은 절대 안됨
        상우하좌 순으로 4방향 탐색 후 선택된 방향도 저장
    2-2) 이동 가능한 경우
        - 루돌프와 충돌처리 및 연쇄 이동 처리까지하고 최종 산타의 이동 처리

3. 라운드 끝나고 살아있는 산타들의 점수 1증가
4. 산타들의 점수 출력

<세부 로직 정리>
** 기절 처리
    1) 기절 배열 stopped에 m+1 값을 넣어줌
    2) 산타 이동시 stopped >= m 이면 이동 불가하도록.
        => 그러면 자연스럽게 다다음턴 부터 이동 가능하게 됨
** 연쇄 이동 로직
    -> 연쇄적으로 충돌이 일어난 가장 마지막 위치에서 시작해 순차적으로 산타를 한칸씩 이동시킴
    1) lastX, lastY를 연쇄 연결된 가장 끝 좌표로 이동
    2) 이 끝 좌표부터 처음위치로 돌아오는 방향으로 밀어주기 진행
    3) firstX, firstY 까지 오면 이 처리는 반복문 밖에서 해주기
"""
n, m, p, c, d = map(int, input().split())
rudolf = list(map(int, input().split()))

score = [0 for _ in range(p + 1)]
position = [(0, 0) for _ in range(p + 1)]
arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
is_live = [False for _ in range(p + 1)]
stopped = [0 for _ in range(p + 1)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

arr[rudolf[0]][rudolf[1]] = -1

# (x, y)가 보드 내의 좌표인지 확인하는 함수
def is_range(x, y):
    # return 1 <= x and x <= n and 1 <= y and y <= n
    return 1 <= x <= n and 1 <= y <= n

for _ in range(p):
    id, x, y = tuple(map(int, input().split()))
    position[id] = (x, y)
    arr[position[id][0]][position[id][1]] = id
    is_live[id] = True

for t in range(1, m + 1):
    closestX, closestY, closestIdx = 10000, 10000, 0

    # 살아있는 산타 중 루돌프에 가장 가까운 산타 찾기
    for i in range(1, p + 1):
        if not is_live[i]:
            continue

        currentBest = ((closestX - rudolf[0]) ** 2 + (closestY - rudolf[1]) ** 2, (-closestX, -closestY))
        currentValue = ((position[i][0] - rudolf[0]) ** 2 + (position[i][1] - rudolf[1]) ** 2, (-position[i][0], -position[i][1]))

        if currentValue < currentBest:
            closestX, closestY = position[i]
            closestIdx = i

    # 가장 가까운 산타의 방향으로 루돌프 이동
    if closestIdx:
        prevRudolf = rudolf
        moveX = 0
        if closestX > rudolf[0]:
            moveX = 1
        elif closestX < rudolf[0]:
            moveX = -1

        moveY = 0
        if closestY > rudolf[1]:
            moveY = 1
        elif closestY < rudolf[1]:
            moveY = -1

        rudolf = [rudolf[0] + moveX, rudolf[1] + moveY]
        arr[prevRudolf[0]][prevRudolf[1]] = 0

    # 루돌프의 이동으로 충돌한 경우, 산타 이동시키고 처리를
    if rudolf[0] == closestX and rudolf[1] == closestY:
        firstX = closestX + moveX * c
        firstY = closestY + moveY * c
        lastX, lastY = firstX, firstY

        stopped[closestIdx] = t + 1 # 기절

        # 이동한 위치에 산타가 있을 경우, 연쇄적으로 이동이 일어남 
        while is_range(lastX, lastY) and arr[lastX][lastY] > 0:
            lastX += moveX
            lastY += moveY

        # 연쇄적으로 충돌이 일어난 가장 마지막 위치에서 시작해 순차적으로 산타를 한칸씩 이동시킴
        while not (lastX == firstX and lastY == firstY):
            beforeX = lastX - moveX
            beforeY = lastY - moveY

            if not is_range(beforeX, beforeY): break

            idx = arr[beforeX][beforeY]

            if not is_range(lastX, lastY):
                is_live[idx] = False # 탈락
            else:
                arr[lastX][lastY] = arr[beforeX][beforeY]
                position[idx] = (lastX, lastY)

            lastX, lastY = beforeX, beforeY

        score[closestIdx] += c # 점수 제공 
        position[closestIdx] = (firstX, firstY)
        if is_range(firstX, firstY):
            arr[firstX][firstY] = closestIdx
        else:
            is_live[closestIdx] = False

    arr[rudolf[0]][rudolf[1]] = -1 # 루돌프 게임판에 표시

    # 각 산타들은 루돌프와 가장 가까운 방향으로 한칸 이동
    for i in range(1, p+1):
        if not is_live[i] or stopped[i] >= t:
            continue

        minDist = (position[i][0] - rudolf[0])**2 + (position[i][1] - rudolf[1])**2
        moveDir = -1

        for dir in range(4):
            nx = position[i][0] + dx[dir]
            ny = position[i][1] + dy[dir]

            if not is_range(nx, ny) or arr[nx][ny] > 0:
                continue

            dist = (nx - rudolf[0])**2 + (ny - rudolf[1])**2
            if dist < minDist:
                minDist = dist
                moveDir = dir

        if moveDir != -1: # 이동 가능한 경우
            nx = position[i][0] + dx[moveDir]
            ny = position[i][1] + dy[moveDir]

            # 산타의 이동으로 충돌한 경우, 산타 이동시키고 처리
            if nx == rudolf[0] and ny == rudolf[1]:
                stopped[i] = t + 1 # 기절

                moveX = -dx[moveDir]
                moveY = -dy[moveDir]

                firstX = nx + moveX * d
                firstY = ny + moveY * d
                lastX, lastY = firstX, firstY

                if d == 1: # 제자리로 돌아감
                    score[i] += d # 점수만 제공
                else:
                    # 만약 이동한 위치에 산타가 있을 경우, 연쇄적으로 이동 일어남
                    while is_range(lastX, lastY) and arr[lastX][lastY] > 0:
                        lastX += moveX
                        lastY += moveY

                    # 연쇄적으로 충돌이 일어난 가장 마지막 위치에서 시작해, 순차적으로 산타를 한칸씩 이동시킴
                    while lastX != firstX or lastY != firstY:
                        beforeX = lastX - moveX
                        beforeY = lastY - moveY

                        if not is_range(beforeX, beforeY):
                            break

                        idx = arr[beforeX][beforeY]

                        if not is_range(lastX, lastY):
                            is_live[idx] = False # 탈락
                        else:
                            arr[lastX][lastY] = arr[beforeX][beforeY]
                            position[idx] = (lastX, lastY)

                        lastX, lastY = beforeX, beforeY

                    score[i] += d # 점수 제공
                    arr[position[i][0]][position[i][1]] = 0
                    position[i] = (firstX, firstY)
                    if is_range(firstX, firstY):
                        arr[firstX][firstY] = i
                    else:
                        is_live[i] = False # 이동한 곳이 범위 밖이면 탈락 처리
            else: # 충돌 안한 경우 그냥 이동만 시키면 됨
                arr[position[i][0]][position[i][1]] = 0
                position[i] = (nx, ny)
                arr[nx][ny] = i

    # 라운드가 끝나고 살아있는 산타들의 점수를 1 증가
    for i in range(1, p+1):
        if is_live[i]:
            score[i] += 1

for i in range(1, p + 1):
    print(score[i], end=" ")