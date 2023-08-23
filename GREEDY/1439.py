# 뒤집기
# 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 함
# 문자열 S가 주어졌을 때, 해야하는 행동의 최소 횟수를 출력
# 입력 예시 : 11001100110011000001 -> 출력 : 4
s = input()
count = 0
if int(s[0]) == 1 : flag = True
else : flag = False

for i in range(len(s)) :
    a = int(s[i-1])
    if a == int(s[i]) : continue
    a = int(s[i])
    if i !=0 and flag != a :
        count += 1       
    i += 1

print(count)
