# 이것이 코딩테스트다 책 - Ch3 그리디 예제 03번) 숫자 카드 게임

# 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
# 룰은 다음과 같다
    # 1. 숫자가 쓰인 카드들이 N*M 형태로 놓여 있다
    # 2. 뽑고자 하는 카드가 포함되어 있는 행 선택
    # 3. 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 함
    # 4. 따라서 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 함

# 방법: (해설과 일치)
    # 각 행마다 가장 작은 수를 선택하여 배열에 추가
    # 선택된 수들 중 가장 큰 수 출력

n, m = map(int, input().split())
arr = []
[arr.append(list(map(int, input().split()))) for _ in range(n)]

tmp = [] # 사실 이렇게 배열에 넣을 필요가 없음
for a in arr :
    min_value = min(a)
    tmp.append(min_value)

print(max(tmp))