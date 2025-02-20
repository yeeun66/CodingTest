# 기둥과 보 설치

# 설치 및 삭제 연산을 요구할 때 마다 일일이 '전체 구조물을 확인하며' 규칙을 확인
# possible() 메서드를 이용하여 현재 구조물이 정상인지를 체크할 수 있도록 하자
#      그래서 매번 연산이 발생할 때 마다, possible() 함수를 호출하여 현재 구조물이 정상인지 체크하고, 
#      정상이 아니라면 현재의 연산을 무시하도록 하자.
#       => 즉 일단, 설치(삭제)한 뒤에 possible 함수로 가능 여부 판단 후,
#         불가능 하면 다시 삭제(설치) 하면 됨

# * 입력 체크
# build_frame: 4개의 원소 (연산 수행, x y a b)
#   x, y: 설치 또는 삭제할 교차점의 좌표 (가로, 세로)
#   a: 구조물의 종류 (0은 기둥, 1은 보)
#   b: 구조물을 삭제할지(0), 설치할지(1)
# (구조물) 교차점 좌표를 기준으로 보는 오른쪽, 기둥은 위쪽 방향으로 설치 또는 삭제함

# * 출력 체크
# return 하는 배열(answer)은 가로(열) 길이가 3인 2차원 배열로, 각 구조물의 좌표를 담고있음
# 배열의 원소는 [x, y, a] 형식 => 가로좌표, 세로좌표, 구조물종류(0,1)
# 배열은 x좌표 기준으로 오름차순 정렬하며, x좌표가 같을 경우 y좌표 기준으로 오름차순 정렬
#     x, y좌표가 모두 같은 경우 기둥이 보보다 앞에 오면 됨

# 설치 가능한 구조물인지 검사
def possible(answer) :
    for x, y, types in answer: 
        if types == 0 : # 기둥일 때
            # 바닥 위에 있거나, 보의 한쪽 끝 부분 위에 있거나(두가지), 또 다른 기둥 위에 있어야 함
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer : 
                continue
            return False
        elif types == 1 : # 보 일 때
            # 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 함
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer) : 
                continue
            return False
        
    return True
    
def solution(n, build_frame):
    answer = []
    for frame in build_frame :
        x, y, types, oper = frame
        if oper == 0 : # 삭제하는 경우
            answer.remove([x, y, types]) # 일단 지우고
            if not possible(answer) : # 불가능하면 다시 설치
                answer.append([x, y, types])
        elif oper == 1 : # 설치하는 경우
            answer.append([x, y, types]) # 일단 설치하고
            if not possible(answer) : # 불가능하면 다시 삭제
                answer.remove([x, y, types])
    
    return sorted(answer)