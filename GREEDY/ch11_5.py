# 이것이 코딩테스트다 책 - Ch11 그리디 기출문제 05번) 볼링공 고르기
# 

N, M = map(int, input().split())
ball = list(map(int, input().split()))

cnt = 0
for i in range(N-1) :
    for j in range(i+1, N) :
        if ball[i] != ball[j] : cnt += 1
print(cnt)