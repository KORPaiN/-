pos = list(input()) #열:abcdefgh, 행:12345678
pos[0] = int(ord(pos[0])) - int(ord('a')) + 1 #col 문자열 -> 10진수 : ord로 진행

pos[1] = int(pos[1]) #row

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

result = 0
for i in range(len(dx)):
    next_col = pos[0] + dx[i]
    next_row = pos[1] + dy[i]

    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result += 1

print(result)
