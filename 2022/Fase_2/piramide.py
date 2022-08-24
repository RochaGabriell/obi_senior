n = int(input())
piramide = []

for i in range(n):
    aux = []
    for j in range(n):
        aux.append(1)
    piramide.append(aux[:])

if n % 2 == 0:
    cont = int(n/2)
else:
    cont = n-1

for x in range(cont):
    for i in range(x, len(piramide)-x):
        for j in range(x, len(piramide)-x):
            piramide[i][j] = x+1
    
for i in piramide:
    print(*i)