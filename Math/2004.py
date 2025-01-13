# 조합 0의 개수
# nCm의 끝자리 0의 개수를 출력하는 프로그램을 작성

# ---- 이 방법은 시간 초과.. 어림도 없음 ---- 애초에 말이 안됨
# nCm 그냥 수식으로 반복문가지고 계산해서
# 끝자리 0개수는 문자열 스택으로 카운트해서 출력하기

# ---- Solution ----
# 분모에서 2x5 세트 갯수가 a이고
# 분자에서 2x5 세트 갯수가 b라면
# 가장 뒤에 오는 0의 갯수는 a-b 이다.
# 위 조건 사용하여 문제 푸는 것임

# 근데 이제 갯수를 어케 구하냐
    # 2의 갯수 구하깅
        # 만약 분모가 5!일 때, 
        # 5// 2 == 2 >> count_two = 2
        # 5// 4 == 1 >> count_two = 3
        # 5// 8 == 0 >> count_two = 3 (종료)
        # ==> 총 2의 갯수는 3개
    # 5의 갯수 구하깅
        # 만약 분모가 5!일 때, 
        # 5// 5 == 1 >> count_fv = 1
        # 5// 25 == 0 >> count_two = 1 (종료)
        # ==> 총 5의 갯수는 1개
    # 이때 분자는 m! 그리고 (n-m)! 으로 2개임
    # 이제 사실상 필요한건 10의 갯수니까 (분모의 2 - 분자의 2) 와 (분모의 5 - 분자의 5) 갯수를 구하여 
    # 작은값을 출력하면 됨

def count_two(x) :
    count = 0
    two = 2
    while x // two:
        count += int(x//two)
        two *= 2
    return count

def count_fv(x) :
    count = 0
    fv = 5
    while x // fv:
        count += int(x//fv)
        fv *= 5
    return count
        

import sys
input = sys.stdin.readline
n, m = map(int, input().split())

two = count_two(n) - count_two(m) - count_two(n-m)
five = count_fv(n) - count_fv(m) - count_fv(n-m)

print(min(two, five))