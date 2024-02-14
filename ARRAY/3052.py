# 배열 연습용
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램

a = []
for _ in range(10) :
    a.append(int(input()))

for i in range(10) :
    a[i] = a[i] % 42

count = len(set(a)) # 중복되지 않은 원소를 얻고자할 때 사용하는 함수 

print(count)