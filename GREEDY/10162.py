# 전자레인지
# A, B, C (5분, 1분, 10초) 3개의 버튼을 적절히 눌러서 그 시간의 합이 정확히 T초가 되도록 최소 버튼 조작
t = int(input())
cnt = [0]*3

while t > 0 :
    if t >= 300 :
        t -= 300
        cnt[0] += 1
    elif t >= 60 :
        t -= 60
        cnt[1] += 1
    elif t >= 10 :
        t -= 10
        cnt[2] += 1
    else : t -= 10

if t == 0 :
    for i in range(3) :
        print(cnt[i], end = ' ')
else : print(-1)