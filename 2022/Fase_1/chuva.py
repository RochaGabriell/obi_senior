n = int(input())
s = int(input())
cont = 0

lista = list(map(int, input().split()))

for i in range(len(lista)):
    for j in range(len(lista)):
        soma = sum(lista[i:j+1])
        if soma == s:
            cont += 1
print(cont)