# 이것이 코딩테스트다 책 - Ch11 그리디 기출문제 01번) 모험가 길드

# 그룹수의 최대 값이니까
# 공포도를 오름차순 정렬하여 최소한의 모험가 수만 포함하여 그룹 결성

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

member = 0
group = 0
for i in arr :
    member += 1
    if i <= member: 
        group += 1
        member = 0

print(group)