# 배열 연습용
# 최대값 M 구하고 모든 점수를 점수/M*100으로 고침
# 계산 후 새로운 평균 구하기

# 첫째 줄에 시험 본 과목의 개수 N
# 둘째 줄에 현재 성적
# 3
# 10 20 30

N = int(input())

a = list(map(int, input().split())) # 입력 받고, 공백 단위로 나눠서 list에 정수형으로 저장하는 코드 (기억하기)

max = -1
for i in range(N) :
    if max < a[i] :
        max = a[i]

for i in range(N) :
    a[i] = a[i]/max*100

sum = sum(a) # list 값 다 더하는 함수 sum
result = sum / N

print(result)