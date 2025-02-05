# 카드 정렬하기

# 방법:
# 1. 카드 묶음의 크기를 오름차순 정렬 한다. (deque로 사용)
    # 처음에는 앞에 두개를 왼쪽에서 pop하여 더한 후 result에 더하고, 데크에 왼쪽에 삽입한다
    # n==1 일 때는 예외처리, 결과:0
# 큐 엠티까지 아래를 반복
# 2. 데크에서 가장 작은 값 두개를 pop한다
    # pop할 때 앞에 2개와 방금 생성된 tmp와 비교
# 3. pop한 두 개의 값을 더한 후 result에 더하고, tmp에 넣는다
# 4. 반복문 나온 후 result 값 출력

# 그냥 처음 두개 뽑고 더한거 큐에 넣고 정렬하고 다시 앞에 두개 뽑고 이런식으로 해야할 것 같음

# ==> 생각한 논리는 맞는데 deque로 넣고 정렬하고 하면 시간 초과 나기 때문에, 
# 우선순위 큐(heapq) 사용하면 해결 가능 !!!

import heapq

N = int(input())
card = []
for _ in range(N) : card.append(int(input()))

result = 0
if N == 1 : 
    print(result)
    exit()

card.sort() # 처음에는 정렬 한 번 해줘야 함
card1 = heapq.heappop(card)
card2 = heapq.heappop(card)

result = card1 + card2
heapq.heappush(card, result)

while len(card) > 1 :

    card1 = heapq.heappop(card)
    card2 = heapq.heappop(card)

    tmp = card1 + card2
    result += tmp
    heapq.heappush(card, tmp)

print(result)