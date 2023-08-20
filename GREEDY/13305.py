# 주유소
# 각 도시에 있는 주유소의 기름 가격과, 각 도시를 연결하는 도로의 길이를 입력 받아 
# 제일 왼쪽 도시에서 제일 오른쪽 도시로 이동하는 최소의 비용을 계산하는 프로그램

n = int(input())
km = list(map(int, input().split()))
price = list(map(int, input().split()))
total = 0
min_price = price[0]
total += min_price * km[0]

for i in range(1, n-1) :
    if min_price > price[i] :
        min_price = price[i]
    total += min_price * km[i]
    
print(total)