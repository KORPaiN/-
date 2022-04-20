n = int(input())
clock = [0,0,0]
# 00:00:00 ~ 23:59:59 = 86400초

count = 1
for i in range(1, (n+1) * 3600):
    clock[2] += 1

    if clock[2] >= 60:
        clock[1] += 1
        clock[2] = 0

    if clock[1] >= 60:
        clock[0] += 1
        clock[1] = 0

    if '3' in str(clock[0]) + str(clock[1]) + str(clock[2]):
        count+=1
    #str 탐색을 이용함 = 십의 자리 숫자에서도 찾을 수 있음
print(count)

#정답 = 3중 for문을 이용해 for문이 돌아가는 순서를 활용
cnt = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1
