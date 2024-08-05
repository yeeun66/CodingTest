# 배열 연습용
# 최대값 M 구하고 모든 점수를 점수/M*100으로 고침
# 계산 후 새로운 평균 구하기

# 첫째 줄에 시험 본 과목의 개수 N
# 둘째 줄에 현재 성적

N = int(input())

a = list(map(int, input().split()))

max = -1

for i in range(N) : 
    if max < a[i] : 
        max = a[i]

for i in range(N) :
    a[i] = a[i] / max * 100

print(sum(a) / N)