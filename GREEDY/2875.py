# 대회 or 인턴
# 여학생 N명, 남학생 M 명중 K명은 반드시 인턴 참가 시키고, 나머지로 최대한 많은 팀 결성
# 한 팀에는 무조건 여2+남1로 이루어짐

'''
로직
6 3 2
2 1
2 1
남은 학생 2 2 -> 2명 참가 -> 끝 

현재 N+M -3 >= K 이면 아래를 반복
N >= 2 이고, M >= 1이면 N -= 2 , M -= 1 하고, team += 1 
위 조건 중 하나라도 충족 안되면 반복 종료 후 team 출력
'''
N, M, K = map(int, input().split())

team = 0
while N+M - 3 >= K : 
    if N >= 2 and M >= 1 : 
        N -= 2
        M -= 1
        team += 1
    else : break

print(team)
