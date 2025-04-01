# 컨베이어 벨트 위의 로봇

# 컨베이어 배열 예시 (deque), 크기 2N
# [(1, False), (2, False), (1, False), (2, False), (1, False), (2, False)]

# 종료 조건까지 아래를 반복 (step=1부터 시작)
    # 1. 배열 회전 시키기
        # deque의 rotate 함수 사용
        # 수행 후, N-1 번째에 로봇이 True라면, False로 바꾸기 (내리는 위치 로봇 내리기)
    # 2. 로봇 이동 시키기
        # N-2 번 부터 0번 순으로 한칸 이동 가능한 상태면 이동
            # 즉 앞 칸의 내구도가 1 이상이고, 로봇 Fasle이면, 
                # 앞 칸의 로봇을 True로 바꾸고, 내구도 -=1 하고, 있던 칸의 로봇은 Fasle로 바꿔
        # 수행 후, N-1 번째에 로봇이 True라면, False로 바꾸기
    # 3. 올리는 위치에 로봇 올리기
        # 현재 0번째 칸의 내구도가 0이 아니면, 그 칸에 로봇을 True로 하고, 내구도 -=1 한다
    # 4. 종료 조건
        # 현재 conv 배열에서 0갯수 세서, K개 이상이면 종료
        # 아니면 step += 1

# 시간 초과.. 
# 해결 >> cnt = sum([1 for i in conv if i[0] == 0])
# 위 코드 반복문에서 이걸로 바꿨더니 해결

from collections import deque
conv = deque()

N, K = map(int, input().split())
arr = list(map(int, input().split()))
for a in arr : conv.append([a, False])

cnt = 0 
step = 0
while cnt < K  : 
    step += 1

    conv.rotate(1)
    if conv[N-1][1] == True : conv[N-1][1] = False

    for i in range(N-2, -1, -1) :
        if conv[i][1] and conv[i+1][0] >= 1 and conv[i+1][1] == False: 
            conv[i+1][1] = True
            conv[i+1][0] -= 1
            conv[i][1] = False
    if conv[N-1][1] == True : conv[N-1][1] = False

    if conv[0][0] > 0 :
        conv[0][1] = True
        conv[0][0] -= 1
    
    cnt = sum([1 for i in conv if i[0] == 0]) # 이거 고쳤다고 시간초과 해결되는게 ... 신기

print(step)