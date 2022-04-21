n, k = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())),reverse = True)

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] < B[j] and k > 0:
            A[i], B[j] = B[j], A[i]
            k -= 1
            break

print(sum(A))

# 정답

for i in range(k):
    if A[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(A))
