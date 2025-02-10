# 이것이 코딩테스트다 책 - Ch4 구현 예제 1-02번) 시각

# 00시 00분 00초 부터 N시 59분 59초 까지 1초씩 증가 시키며 문자열로 3이 포함되면 cnt 증가시킨다
# 그럼 반복문이 24*60*60로 3중 반복문을 통해 계산할 수 있다

N = int(input())
time = ''
cnt = 0
for i in range(N+1) :
    for j in range(60) :
        for k in range(60) :
            if '3' in str(i) + str(j) + str(k) : 
                cnt += 1

print(cnt)