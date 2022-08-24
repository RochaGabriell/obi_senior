n = int(input())
quadrado = []
linha = coluna = linha_zero = 0

for i in range(n):
    quadrado.append(list(map(int, input().split())))

for i in range(n):
    if 0 not in quadrado[i]:
        soma_aux = 0
        for s in quadrado[i]:
            soma_aux += s
        soma = soma_aux

for i in range(n):
    for j in range(n):
        if quadrado[i][j] == 0:
            linha = i
            coluna = j
            for s in quadrado[i]:
                linha_zero += s
            soma = soma_aux

falta = soma - linha_zero

print(f"{falta}\n{linha+1}\n{coluna+1}")