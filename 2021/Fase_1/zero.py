# https://olimpiada.ic.unicamp.br/pratique/ps/2021/f1/zero/

n = int(input())
lista = []

for i in range(n):
    ln = int(input())
    if ln == 0:
        if len(lista) > 0:
            lista.pop()
    else:
        lista.append(ln)

print(sum(lista))