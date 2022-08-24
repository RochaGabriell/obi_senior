# https://olimpiada.ic.unicamp.br/pratique/ps/2021/f1/torneio/
cont = 0
for i in range(0, 6):
    n = str(input())
    if n == "V":
        cont += 1

if cont == 0:
    print("-1")
elif 1 >= cont <= 2:
    print("1")
elif 3 >= cont <= 4:
    print("2")
elif 5 >= cont <= 6:
    print("3")