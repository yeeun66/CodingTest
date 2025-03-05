# 이것이 코딩테스트다 책 - Ch11 그리디 기출문제 03번) 문자열 뒤집기
# 모두 0으로 만드는 경우와 모든 1로 만드는 경우를 따로 구하고, 그 중 작은 값을 출력

# 문자열이 0001100 일 때,
    # 모두 0으로 만드는 경우 -> 총 1회
    # 모두 1로 만드는 경우 -> 총 2회
    # 따라서 최소는 총 1회

# 로직: 
# 모두 0으로 만드는 경우, 1로 만드는 경우를 변수 2개로 따로 저장한다
# 우선 첫번째 문자열 처리
    # 1이면 cnt0 += 1
    # 0이면 cnt1 += 1
# 문자열 마지막에서 두번째까지
    # 다음 문자열이랑 현재랑 다르고,
        # 1로 바뀔 때 -> cnt0 +=1
        # 0으로 바뀔 때 -> cnt1 += 1

data = input()

cnt0, cnt1 = 0, 0

if data[0] == '1' : cnt0 += 1
else : cnt1 += 1

for i in range(len(data)-1) : 
    if data[i] != data[i+1] :
        if data[i+1] == '1' : cnt0 += 1
        else : cnt1 += 1

print(min(cnt0, cnt1))