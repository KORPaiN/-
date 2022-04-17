n, k = map(int, input().split())

for i in range(1, n+1):

    if n % k == 0:
        n //= k
    else:
        n -= 1
    if n == 1:
        break

print(i)

#시간 복잡도 감소
n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)
