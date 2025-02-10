# 프로그래머스 60057번 (just 문자열 구현) 
# >>> 2020 카카오 공채 코테 1번 (난이도: 하, 정답률 25%)
# 초기 min 값을 len(s) 로 설정 후, 1개로 잘랐을 때 부터 len(s)개로 잘랐을 때 새로 변형된 문자열의 갯수를 최소로 업데이트 한다
    # 이 때 문자열 압축(변형) 방법:
    # 현재 값을 기준으로 오른쪽 값이 같으면 카운트 한다 (이 때, 현재 값과 같은 길이로 점프 하면서 카운트)
    # 오른쪽 값이 다를 때 까지 계속 카운트 후
        # 최종 카운트가 1이라면 그냥 그 문자만 새로운 문자에 추가 (+)
        # 카운트가 1이상이면 앞에 카운트를 붙이고 해당 문자도 추가 (+)
        # 그리고 카운트가 끝났을 때 멈춰진 위치부터 다시 시작해야 하므로 저장해둔다

def solution(s):
    answer = len(s)
    for i in range(1, len(s)) :
        new = ''
        gap = i 
        start = i
        cnt = 1
        a = s[0:gap]
        for j in range(start, len(s), gap) :
            if a == s[j: j+gap] : cnt += 1
            else : 
                if cnt == 1 : new += a
                else : new += str(cnt) + a
                a = s[j:j+gap]
                cnt = 1
        if cnt == 1 : new += a
        else : new += str(cnt) + a
        
        answer = min(answer, len(new))
           
    return answer