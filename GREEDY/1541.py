# 잃어버린 괄호 
# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램

# 55-50+40

# - 기준으로 문자열 분리
# 고려해야 할 경우 2가지
    # 1. 맨 앞이 -일 경우 -44-20+4
    # 2. 맨 앞이 0일 경우 

a = input()
b = a.split('-') # [55, 50+40]

result = 0
# 첫번째 따로 작업 (맨 앞이 -일 경우 / + 밖에 없을 경우)
x = sum(map(int, (b[0].split('+'))))

if a[0] == '-' :
    result -= x
else :
    result += x

for i in b[1: ] :
    x = sum(map(int, (i.split('+'))))
    result -= x

print(result)