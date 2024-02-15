# 설탕 배달 (Greedy)
# 5키로 비닐, 3키로 비닐 / 최대한 적은 비닐로 /  정확히 n키로 만들 수 없다면 -1 출력

n = int(input())
f = 0 # 5kg 봉지 개수
t = 0 # 3kg 
m = n // 5 # 5로 나눈 몫

if n % 5 == 0 : f = m
else :
    while True:
        if (n - 5*m) % 3 == 0 :
            t = (n-5*m) / 3
            f = m
            break
        elif m == 0 :
            f = -1
            break
        m -= 1
        
print(int(f + t))
# 내일 다시 풀기 