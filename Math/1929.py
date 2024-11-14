# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 시간 초과 -> 당연히 끝까지 다 찾으면 O(N)이겠지..

# 에레토스테네스의 체 를 구글링 해보고 다시 푸세요
# 2부터 √n까지 나누어 떨어지면 해당 배열의 원소 삭제

M, N = map(int, input().split())

for i in range(M, N+1) :
    if i == 1 : continue
    if i == 2 : 
        print(i)
        continue
    
    max = int(i**(1/2))
    flag = 0
    for j in range(2, max+1) :
        if i % j == 0 : 
            flag = 1
            break
    if not flag : print(i)