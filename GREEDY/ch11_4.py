# 이것이 코딩테스트다 책 - Ch11 그리디 기출문제 04번) 만들 수 없는 금액
# 
# 동전들은 배열에 오름차순 정렬 coins
# 최솟값 (result)은 1부터 시작하여 다음을 반복
    # coins에서 하나씩 꺼내서 result를 만들 수 있는지 확인한다
    # 이때 result < coin 이면 result를 만들 수 없으므로 반복문 중단 후 result 출력한다
    # result를 만들 수 있다면 result += coin을 한다
    # 그럼 이제 다시 만들어진 result가 검사 대상이고, 그 이전까지는 모두 만들 수 있다. 

n = int(input())
coins = list(map(int, input().split()))
coins.sort()

result = 1
for coin in coins :
    if result < coin : break
    result += coin # 검사 대상

print(result)