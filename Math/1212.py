# 8진수 -> 2진수

# 입력 받은 8진수를 앞에서부터 하나씩 변환해준다
    # 이 때, 4보다 크면 앞자리는 무조건 1 (이때 크면은 모두 크거나 같다는 뜻.. 편의상)
        # 이제 여기서 4를 빼고 남은 것 값이 2보다 크면 두번째 자리도 1
        # 이제 2를 빼고 남은 것이 1보다 크면 세번째 자리에도 1
        # 각 stage 마다 해당 조건보다 작으면 그 자리는 0으로 세팅
# 출력 전에 고려할 것 : 입력 받은 8진수가 0이 아닌한, 맨 앞자리는 1이어야 함. 즉 앞에 나오는 0 생략 => 걍 int 로 바꾸면 됨 

import sys
input = sys.stdin.readline

num = input().strip()
output = []
for i in num:
    result = ''
    n = int(i)
    if n >= 4 : 
        result += '1'
        n -= 4
    else : result += '0'

    if n >= 2:
        result += '1'
        n -= 2
    else : result += '0'

    if n >= 1:
        result += '1'
        n -= 1
    else : result += '0'
    output.append(result)

outputs = "".join(output) # str
print(int(outputs))