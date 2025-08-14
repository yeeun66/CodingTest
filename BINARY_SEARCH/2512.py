# 예산
'''
예제 입력 
110 120 140 150
485

start = 0, end = 150 -> mid = 75
75 75 75 75 ==> 300 (total보다 작으니까 오른쪽으로 서치)

start = 76, end = 150 -> mid = 113
110 113 113 113 ==> 449 (total보다 작으니까 오른쪽으로 서치)

start = 114, end = 150 -> mid = 132
110 120 132 132 ==> 494 (total보다 크니까 왼쪽으로 서치)

start = 114, end = 131 -> mid = 122 
110 120 122 122 ==> 474 (total보다 작으니까 오른쪽으로 서치)

start = 123, end = 131 -> mid = 127
110 120 127 127 ==>  484 (total보다 작으니까 오른쪽으로 서치)

start = 128, end = 131 -> mid = 129
110 120 128 128 ==> 486 (total보다 크니까 왼쪽으로 서치)

start = 128, end = 128 -> mid = 128 
110 120 128 128 ==> 486 (total보다 크니까 왼쪽으로 서치)

start = 128, end = 127 -> start > end 인 상황 (mid 출력 후 종료)

'''
'''
로직
1. 각 지방마다 예산 합이 총 예산보다 작거나 같으면, 그냥 그 중 최댓값 출력
2. 예산 합이 총 예산보다 크면, 이진 탐색으로 상한 값 찾기 
    (1) start = 0, end = max_v로 시작해서 (start <= end) 인 동안 아래를 반복
    (2) mid 계산.
        mid로 계산한 총합이 
        - total보다 작으면, 오른쪽으로 서치 (start = mid +1)
        - total보다 크면, 왼쪽으로 서치 (end = mid -1)
    (3) 반복문 나오면 최종 start와 end의 mid를 출력

'''

import sys; input = sys.stdin.readline
N = int(input())
city = list(map(int, input().split()))
total = int(input())

sums = sum(city)
if sums <= total : 
    print(max(city))
    exit()

def binary_search(target, start, end) : 

    while start <= end : 
        mid = (start + end) // 2
        tmp = 0
        for i in range(N) : 
            if city[i] >= mid : tmp += mid
            else : tmp += city[i]
        
        if tmp < total : start = mid + 1
        elif tmp == total : return mid
        else : end = mid - 1 
    
    return (start + end) // 2

result = binary_search(total, 0, max(city)) 
print(result)