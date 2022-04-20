n = int(input())
mo = list(map(int, input().split()))
'''
mo.sort()
answer = 0

while(len(mo) != 0):

    for i in range(mo[0]):
        mo.pop(0)

    answer += 1

print(answer)
'''

# 정답
result = 0 #총 그룹수
count = 0 #현재 그룹에 포함된 모험가 수

for i in mo: #공포도를 낮은 순으로 정렬하여 하나씩 확인
    count += 1 #현재 그룹에 해당 모험가 포함
    if count >= i: #현재그룹에 포함된 모험가의 수 > 공포도 : 그룹 결성
        result += 1 # 그룹 수 증가
        count = 0 # 모험가 수 초기화

print(result)
