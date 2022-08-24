"""
C = CONSUMO EM KM POR LITRO
D = DISTÂNCIA DO AEROPORTO EM KM
T = COMBUSTIVEL PRESENTE
"""

c = int(input())
d = int(input())
t = int(input())

cal = d / c
if cal <= t:
    print(0.0)
else:
    cont = cal - t
    print(f"{cont:.1f}")