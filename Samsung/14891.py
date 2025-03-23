# 톱니바퀴
# 톱니바퀴의 초기 상태와 톱니바퀴를 회전시킨 방법이 주어졌을 때, 최종 톱니바퀴의 상태를 구하는 프로그램을 작성
# 
# 1. 입력 받기
    # 2차원 배열 arr -> 4개의 톱니바퀴 상태 (N극은 0, S극은 1)
    # 회전 횟수 K
    # 회전 방법 K번 주어짐 (톱니바퀴의 번호, 방향) # 시계방향은 1, 반시계는 -1

# 2. K번 회전 시키기 (아래를 K번 반복)
    # num, direct = 회전시킬 번호와 방향 입력 받고 rotate와 method에 넣기
    # 2-1. method에 동시에 회전할 톱니바퀴들 수집 
        # method empty 까지 다음을 반복
            # popleft해서 현재 num을 기준으로 양방향 검사, 회전 해야할 톱니바퀴 있으면, 
            # method랑 rotate 배열에 추가 (번호랑, 방향 바꿔서)
    # 2-2. rotate 배열에 있는 바퀴들 동시에 회전시키기
        # 시계 방향: 끝에거 pop해서 앞에 appendleft
        # 반시계: 첫번째꺼 popleft 해서 뒤에 append

# 3. 최종 상태에서 점수 계산 후 출력

from collections import deque

arr = [deque(map(int, input().strip())) for _ in range(4)]
K = int(input())
method = deque()
rotate = [] # 동시에 회전 시킬 톱니바퀴들 수집

for _ in range(K) :
    x, y = map(int, input().split())
    method.append([x, y])
    rotate.append([x, y])
    visited = [False] * 4
    
    while method : 
        num, direct = method.popleft()
        visited[num-1] = True

        # 양 옆 상태 확인
        if num != 1 : # 왼쪽 확인
            if visited[num-2] == False : 
                if arr[num-1][6] != arr[num-2][2] :
                    method.append([num-1, -direct])
                    rotate.append([num-1, -direct])
                    visited[num-2] = True
        if num != 4 : # 오른쪽 확인
            if visited[num] == False : 
                if arr[num-1][2] != arr[num][6] :
                    method.append([num+1, -direct])
                    rotate.append([num+1, -direct])
                    visited[num] = True
    
    # 바퀴들 동시에 회전시키기
    while rotate :
        num, direct = rotate.pop()
        
        if direct == 1 : # 시계 방향
            tmp = arr[num-1].pop()
            arr[num-1].appendleft(tmp)
        else: # 반시계
            tmp = arr[num-1].popleft()
            arr[num-1].append(tmp)

result = 0
if arr[0][0] == 1 : result += 1    
if arr[1][0] == 1 : result += 2 
if arr[2][0] == 1 : result += 4
if arr[3][0] == 1 : result += 8

print(result)    