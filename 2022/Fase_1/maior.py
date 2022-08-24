n = int(input())
m = int(input())
s = int(input())
maior = 0

for i in range(m, n, -1):
    soma = 0
    x = i
    while x > 0:
        soma += x % 10
        x = x // 10
    if soma == s:
        maior = i
        break

print(maior) if maior != 0 else print(-1)