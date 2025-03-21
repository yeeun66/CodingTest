# 시험 감독

# 약간 그리디
# 반복문 한번만 돌면서
    # 값이 0보다 크면, main 감독관 만큼 빼고 cnt 1증가 시킴
    # 그래도 0보다 크면 sub 감독관이 사용될 수를 cnt에 증가시킴
        # 이 때 식은 sub 감독관으로 나누어 떨어지면 -> arr[i] / sub
        # 아니라면 -> (arr[i] / sub) + 1
        
N = int(input())
arr = list(map(int, input().split()))
main, sub = map(int, input().split())

cnt = 0
for i in range(N) :
    if arr[i] > 0 : 
        arr[i] -= main
        cnt += 1
    if arr[i] > 0 : 
        if arr[i] % sub == 0 : 
            cnt += int(arr[i] / sub)
        else : cnt += int(arr[i] / sub) + 1
print(cnt)