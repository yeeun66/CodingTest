# 이것이 코딩테스트다 책 - Ch3 그리디 예제 02번) 큰 수의 법칙

# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만들 수 있는 법칙
# 단, 배열의 특징한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 는 없다
# 이때 수가 같더라도 인덱스가 다르면 다른 수로 취급해 연속하여 더할 수 있다 
# 배열의 크기 N, 더해지는 횟수 M, 그리고 K 가 주어졌을 때 큰 수의 법칙에 따른 결과 출력

# 그리디 알고리즘 (내 방법론)
# 배열을 입력 받고 정렬한다
# 특정 인덱스의 수가 K번을 '연속하여' 더할 수는 없으므로, 한칸 건너 다시 더하는 건 상관 없다는 뜻
    # 따라서 가장 큰 수와, 두번째로 큰 수를 저장한 후 K번을 초과할 때 한번 두번째 수 더해주고 다시 가장 큰수를 더해주는 식으로 M번을 더하면 된다
    # 이때 M번 더했다는 표시로 더할 때 마다 M을 1씩 차감하면 된다

# 문제 해설1 (단순 답안): 가장 큰 수를 K번 더하고 두 번째로 큰 수를 한 번 더하는 연산을 반복하면 됨

# solution 1
N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

first = arr[-1]
second = arr[-2]

result = 0

while True :
    for _ in range(K) :
        if M == 0 : break
        result += first
        M -= 1
    if M == 0 : break

    result += second
    M -= 1

print(result)

# 문제 해설2 (시간초과 대비 수학적 아이디어 사용) : 반복되는 수열에 대해서 파악한 하기
    # 가장 큰 수가 더해지는 횟수를 수식으로 계산한 후 그만큼 가장 큰 수를 곱하여 더한 후,
    # 남은 수 만큼 두번째로 큰 수를 곱하여 더해준다 

# solution 2
N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

first = arr[-1]
second = arr[-2]

result = 0

count = int(M / (K+1)) * K
count += M % (K+1) # M이 K+1로 나누어 떨어지지 않을 때 나머지 더해줌

result += count * first
result += (M-count) * second

print(result)