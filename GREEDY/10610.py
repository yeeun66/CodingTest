# 30
# n에 포함된 숫자들을 섞어 30의 배수가 되는 가장 큰 수를 계산하는 프로그램
# 못 만들면 -1 출력
# 예시 102 -> 210 # 80875542 -> 88755420

# 30배수 판정하기
# 1. 10배수: 끝자리가 0이어야 함 ( 0 하나라도 없으면 return -1 )
# 2. 3배수: 각 자리수의 합이 3배수 (재배열과 상관 X)
# 최대값 찾기 : 거꾸로 sorting

def thirty(num) :
    sum = 0
    if '0' not in num :
        return -1
    for i in range(len(num)) :
        sum += int(num[i])
    if sum % 3 == 0 :
        sorted_num = sorted(num, reverse=True)
        r = "".join(sorted_num)
        return r
    else : return -1
    
n = input()
print(thirty(n))