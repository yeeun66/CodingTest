# 주사위 윷놀이

"""
로직
얻을 수 있는 점수의 최댓값 => 백트래킹으로 모든 경우 탐색해서 최댓값 구하기
말 4개, 주사위 10번 굴림, 주사위에서 나온 수는 미리 주어짐
0. 게임판 관리
(0) - 2 - 4 - 6 - 8 - 10 - 12 - 14 - 16 - 18 - 20 - 22 - 24 - 26 - 28 - 30 - 32 - 34 - 36 - 38 - 40 - (도착) <- arr1
                      13 - 16 - 19 - 25        22 - 24 - 25             28 - 27 - 26 - 25 <- arr2, 3, 4
                                               
(25) - 30 - 35 - 40 - (도착) <- 내부는 여기서 경로 합쳐짐 <- arr5

1. 백트래킹 사용해서 게임 진행하며 10번동안 옮겨질 말의 번호 (1~4) 구하기
    - 백트래킹으로 모든 조합 만들어서, 그거 10개로 이동 수행 -> 최대 업데이트 
        - 이랬는데 만약에 시간초과 나면, 사용하는 말의 갯수로..?
    - 옮겨질 수 있는 말의 조건:
        1) 아직 도착하지 않음 (이동 후 도착되는건 상관없음)
        2) 이동 마치는 칸에 다른 말이 있지 않음

2. 말의 이동 
    1) 아직 도착하지 않은지 체크 >> piece[n][0] != -1
        - 도착했다면 리턴 
    2) 배열에서 주사위 칸 만큼 이동
        - arr1일 때, 주사위 칸 만큼 이동 
            - 이동한 칸이 인덱스 초과면, 도착 처리
            - 도착한 칸이 10이면 arr2로, 20이면 arr3로, 30이면 arr4로 변경 (모든 상태는 5번에서 업데이트)
            - 40보다 크면, 도착 처리
        - arr2~4일 때, 
            - 이동해도 인덱스 내부라면, 주사위 칸만큼 이동
            - 인덱스 초과면, 최대한 이동하고 arr5에서 마저 이동
        - arr5일 때
            - 이동해도 인덱스 내부라면, 주사위 칸만큼 이동
            - 인덱스 초과면, 도착 처리 (40보다 큰 값 부여)
    3) 이동한 곳에 다른 말이 있다면, return 
        - tmp_move = (배열번호1~5, 현재 배열에서 인덱스)
    4) 이동 가능할 때, 도착한 곳이 40 이하라면, 점수에 추가
        - 40보다 크면, 도착 처리 piece[n] = (-1, -1)
    5) 최종 도착하지 않은 말 상태 업데이트 (배열번호1~5, 현재 배열에서 인덱스)
        - 도착한 칸이 10이면 arr2로, 20이면 arr3로, 30이면 arr4로 변경

3. 말이 이동 마칠 때 마다 칸의 점수 추가됨: score에 더하기
4. 10번의 턴이 진행된 후, 최종 score와 현재 맥시멈 score중 큰 값을 저장
5. 모든 경우의 수 끝나면 최종 맥시멈 스코어 출력
"""

arr1 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]  # 40끼리도 같은 경로 처리 해야함
arr2 = [10, 13, 16, 19, 25]
arr3 = [20, 22, 24, 25]
arr4 = [30, 28, 27, 26, 25]
arr5 = [25, 30, 35, 40] # 그냥 인덱스 관리 때문에 45 넣어둠 

max_score = 0
dice = list(map(int, input().split()))
     
def move_piece(selected) :
    global max_score
    piece = []
    for i in range(4) : piece.append([1, 0]) # (배열번호1~5, 현재 배열에서 인덱스)

    score = 0
    for i in range(10) :
        n = selected[i] #선택된 말의 번호 1~4
        a, idx = piece[n]
        if (a, idx) == (-1, -1) : return
        cnt = dice[i] # 이동할 칸의 수 

        dest_val = 0
        tmp_arr = a
        tmp_idx = idx + cnt # 이동할 곳 
        if a == 1 : 
            if tmp_idx > 20 : dest_val = 45 # 도착
            else : dest_val = arr1[tmp_idx]

            if dest_val == 10 : tmp_arr, tmp_idx = 2, 0
            elif dest_val == 20 : tmp_arr, tmp_idx = 3, 0
            elif dest_val == 30 : tmp_arr, tmp_idx = 4, 0
            elif dest_val == 40 : tmp_arr, tmp_idx = 5, 3 # 40 같은 경로로 통합 처리 
        
        elif a == 2 : 
            if tmp_idx > 4 : 
                term = tmp_idx - 4
                if term < 4 : 
                    tmp_arr, tmp_idx = 5, term
                    dest_val = arr5[term]
                else : dest_val = 45 # 도착
            else : dest_val = arr2[tmp_idx]

        elif a == 3 :
            if tmp_idx > 3 : 
                term = tmp_idx - 3
                if term < 4 : 
                    tmp_arr, tmp_idx = 5, term
                    dest_val = arr5[term]
                else : dest_val = 45 # 도착
            else : dest_val = arr3[tmp_idx]

        elif a == 4 : 
            if tmp_idx > 4 : 
                term = tmp_idx - 4
                if term < 4 : 
                    tmp_arr, tmp_idx = 5, term
                    dest_val = arr5[term]
                else : dest_val = 45 # 도착
            else : dest_val = arr4[tmp_idx]

        elif a == 5 :
            if tmp_idx > 3 : dest_val = 45 # 도착
            else : dest_val = arr5[tmp_idx]
        
        # 3) 최종 도착은 안했는데, 이동한 곳에 다른 말이 있다면, return 
        if (tmp_arr, tmp_idx) != (-1, -1) and [tmp_arr, tmp_idx] in piece : return 
        
        # 4) 이동 가능할 때, 도착한 곳이 40 이하라면, 점수에 추가
        if dest_val <= 40 : score += dest_val
        else : tmp_arr, tmp_idx = -1, -1 # 도착 처리 

        # 5) 말 상태 업데이트 (배열번호1~5, 현재 배열에서 인덱스)
        piece[n] = [tmp_arr, tmp_idx]

    max_score = max(max_score, score)
    
def backtrack(): # 조합 제작
    # array가 10개가 되면 할 작업
    if len(array) == 10:
        move_piece(array)
        return 

    # 백트래킹 array에 원소 담기 (재귀)
    for i in range(4) : 
        array.append(i)
        backtrack()
        array.pop()

array = []
backtrack()
print(max_score)